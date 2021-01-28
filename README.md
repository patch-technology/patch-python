# Patch Python SDK
![Test](https://github.com/patch-technology/patch-python/workflows/Test/badge.svg)
[![Library Version](https://badge.fury.io/rb/patch_ruby.svg)](https://badge.fury.io/rb/patch_ruby)
[![Discord](https://img.shields.io/discord/733029448558837792)](https://discord.gg/AU8543D)

The official Python library for the [Patch API](https://www.usepatch.com).

## Documentation
For a complete API reference, check out [Patch's API Reference.](https://docs.usepatch.com/).

## Installation

Add the library to your `requirements.txt` file:
```txt
patch >= 1.0.0
```

Then run:
```shell
pip install
```

Or install it directly with
```shell
pip install patch_api
```

### Requirements
- Python 3.0.0

## Usage

### Configuration

After installing the gem, you'll have to initialize it with your API key which is available from the API key page in the Patch dashboard:

```python
import patch_api

api_client = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
```

The `api_client` will be used to instantiate other API objects for Patch resources, for example the `OrdersApi`:

```
import patch_api
from patch_api.api.orders_api import OrdersApi as Orders

api_client = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
orders_api = Orders(api_client=api_client)
```

### Orders
In Patch, orders represent a purchase of carbon offsets or negative emissions by mass. Place orders directly if you know the amount of carbon dioxide you would like to sequester. If you do not know how much to purchase, use an estimate.

In Patch, orders represent a purchase of carbon offsets or negative emissions by mass.
Place orders directly if you know the amount of carbon dioxide you would like to sequester.
If you do not know how much to purchase, use an estimate.
You can also create an order with a maximum desired price, and we'll allocate enough mass to
fulfill the order for you.

[API Reference](https://docs.usepatch.com/#/?id=orders)

#### Examples
```python
import patch_api
from patch_api.api.orders_api import OrdersApi as Orders

api_client = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
orders_api = Orders(api_client=api_client)

# Create an order - you can create an order
# providing either mass_g or total_price_cents_usd, but not both

# Create order with mass
orders_api.create_order(opts={'mass_g': 1_000_000}) # Pass in the mass in grams (i.e. 1 metric tonne)

# Create an order with maximum total price
total_price_cents_usd = 5_00 # Pass in the total price in cents (i.e. 5 dollars)
orders_api.create_order(opts={'total_price_cents_usd': total_price_cents_usd})

## You can also specify a project-id field (optional) to be used instead of the preferred one
project_id = 'pro_test_1234' # Pass in the project's ID
orders_api.create_order(opts={'project_id': project_id, 'mass_g': mass_g})

## Orders also accept a metadata field (optional)
metadata = {user: "john doe"}
orders_api.create_order(opts={'metadata': metadata, 'mass_g': mass_g})

# Retrieve an order
order_id = 'ord_test_1234' # Pass in the order's id
orders_api.retrieve_order(id=order_id)

# Place an order
order_id = 'ord_test_1234' # Pass in the order's id
orders_api.place_order(id=order_id)

# Cancel an order
order_id = 'ord_test_1234' # Pass in the order's id
orders_api.cancel_order(id=order_id)

# Retrieve a list of orders
page = 1 # Pass in which page of orders you'd like
orders_api.retrieve_orders(page=page)
```

### Estimates
Estimates allow API users to get a quote for the cost of compensating a certain amount of CO2. When creating an estimate, an order in the `draft` state will also be created, reserving the allocation of a project for 5 minutes. If you don't place your draft order within those 5 minutes, the order will automatically be cancelled.

[API Reference](https://docs.usepatch.com/#/?id=estimates)

#### Examples
```python
import patch_api
from patch_api.api.estimates_api import EstimatesApi as Estimates

api_client = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
estimates_api = Estimates(api_client=api_client)

# Create an estimate

mass_g = 1_000_000 # Pass in the mass in grams (i.e. 1 metric tonne)
estimates_api.create_estimate(opts={'mass_g': mass_g})

## You can also specify a project-id field (optional) to be used instead of the preferred one
project_id = 'pro_test_1234' # Pass in the project's ID
estimates_api.create_estimate(opts={'mass_g': mass_g, 'project_id': project_id})

# Retrieve an estimate
estimate_id = 'est_test_1234'
estimates_api.retrieve_estimate(id=estimate_id)

# Retrieve a list of estimates
page = 1 # Pass in which page of estimates you'd like
estimates_api.retrieve_estimates(page=page)
```

### Projects
Projects are the ways Patch takes CO2 out of the air. They can represent reforestation, enhanced weathering, direct air carbon capture, etc. When you place an order via Patch, it is allocated to a project.

[API Reference](https://docs.usepatch.com/#/?id=projects)

#### Examples
```python
import patch_api
from patch_api.api.projects_api import ProjectsApi as Projects

api_client = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
projects_api = Projects(api_client=api_client)

# Retrieve a project
project_id = 'pro_test_1234' # Pass in the project's ID
projects_api.retrieve_project(id=project_id)

# Retrieve a list of projects
page = 1 # Pass in which page of projects you'd like
projects_api.retrieve_projects(page=page)
```

### Preferences
Preferences are how you route your orders in Patch. If you don't have a preference, Patch will allocate your order to the least expensive option. If you do have a preference, all of your orders will be sent to that project. You can set your preferences via API, or through the [Patch Dashboard](https://dashboard.usepatch.com/projects).

[API Reference](https://docs.usepatch.com/#/?id=preferences)

#### Examples
```python
import patch_api
from patch_api.api.preferences_api import PreferencesApi as Preferences

api_client = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
preferences_api = Preferences(api_client=api_client)

# Create a preference

project_id = 'pro_test_1234' # Pass in the project_id for your preference
preferences_api.create_preference(opts={'project_id': project_id})

# Retrieve a preference
preference_id = 'pre_test_1234' # Pass in the preferences's id
preferences_api.retrieve_preference(preference_id=preference_id)

# Delete a preference
preference_id = 'pre_test_1234' # Pass in the preferences's id
preferences_api.delete_preference(preference_id=preference_id)

# Retrieve a list of preferences
page = 1 # Pass in which page of preferences you'd like
preferences_api.retrieve_preferences(page=page)
```

## Development

### Running tests

Set up the required environment variable:
```
$ export SANDBOX_API_KEY=<SANDBOX API KEY>
```

Run tests:
```
$ make test
```

To run an individual test:
```
$ python -m unittest
```

### Testing the built package locally

To build the library locally, run:
```
$ make build
```

In another directory, create a file called `patch.py` and install the local package in this directory:

```
$ touch patch.py
$ pip install ../patch-python
```

Set up the required environment variable:
```
$ export SANDBOX_API_KEY=<SANDBOX API KEY>
```

To test the package locally, create a python file in a sibling directory and add the following:
```python
import os
import patch_api

# ..... your Patch API code goes here. See example below:

from patch_api.api.orders_api import OrdersApi as Orders

api_client = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
orders = Orders(api_client=api_client)

list_orders = orders.retrieve_orders(opts={'page': 1})

# Prints your organization's orders
print(list_orders)
```
