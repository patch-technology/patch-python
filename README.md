# Patch Python SDK
![Test](https://github.com/patch-technology/patch-python/workflows/Test/badge.svg)
[![PyPI version](https://badge.fury.io/py/patch-api.svg)](https://badge.fury.io/py/patch-api)
[![Discord](https://img.shields.io/discord/733029448558837792)](https://discord.gg/AU8543D)

The official Python library for the [Patch API](https://www.usepatch.com).

## Documentation
For a complete API reference, check out [Patch's API Reference.](https://docs.usepatch.com/).

## Installation

Add the library to your `requirements.txt` file:
```txt
patch_api >= 1.0.0
```

Then run:
```shell
pip install -r requirements.txt
```

Or install it directly with
```shell
pip install patch-api
```

### Requirements
- Python 3.6.0

## Usage

### Configuration

After installing the gem, you'll have to initialize it with your API key which is available from the API key page in the Patch dashboard. The `patch` object will be used to to make calls to the Patch API:

```python
import patch_api

patch = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
orders = patch.orders.retrieve_orders()
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

patch = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))

# Create an order - you can create an order
# providing either mass_g or total_price_cents_usd, but not both

# Create order with mass
patch.orders.create_order(mass_g=1_000_000) # Pass in the mass in grams (i.e. 1 metric tonne)

# Create an order with maximum total price
total_price_cents_usd = 5_00 # Pass in the total price in cents (i.e. 5 dollars)
patch.orders.create_order(total_price_cents_usd=total_price_cents_usd)

## You can also specify a project-id field (optional) to be used instead of the preferred one
project_id = 'pro_test_1234' # Pass in the project's ID
patch.orders.create_order(project_id=project_id, mass_g=mass_g)

## Orders also accept a metadata field (optional)
metadata = {user: "john doe"}
patch.orders.create_order(metadata=metadata, mass_g=mass_g)

# Retrieve an order
order_id = 'ord_test_1234' # Pass in the order's id
patch.orders.retrieve_order(id=order_id)

# Place an order
order_id = 'ord_test_1234' # Pass in the order's id
patch.orders.place_order(id=order_id)

# Cancel an order
order_id = 'ord_test_1234' # Pass in the order's id
patch.orders.cancel_order(id=order_id)

# Retrieve a list of orders
page = 1 # Pass in which page of orders you'd like
patch.orders.retrieve_orders(page=page)
```

### Estimates
Estimates allow API users to get a quote for the cost of compensating a certain amount of CO2. When creating an estimate, an order in the `draft` state will also be created, reserving the allocation of a project for 5 minutes. If you don't place your draft order within those 5 minutes, the order will automatically be cancelled.

[API Reference](https://docs.usepatch.com/#/?id=estimates)

#### Examples
```python
import patch_api

patch = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))

# Create an estimate

mass_g = 1_000_000 # Pass in the mass in grams (i.e. 1 metric tonne)
patch.estimates.create_estimate(mass_g=mass_g)

## You can also specify a project-id field (optional) to be used instead of the preferred one
project_id = 'pro_test_1234' # Pass in the project's ID
patch.estimates.create_estimate(mass_g=mass_g, project_id=project_id)

# Retrieve an estimate
estimate_id = 'est_test_1234'
patch.estimates.retrieve_estimate(id=estimate_id)

# Retrieve a list of estimates
page = 1 # Pass in which page of estimates you'd like
patch.estimates.retrieve_estimates(page=page)
```

### Projects
Projects are the ways Patch takes CO2 out of the air. They can represent reforestation, enhanced weathering, direct air carbon capture, etc. When you place an order via Patch, it is allocated to a project.

[API Reference](https://docs.usepatch.com/#/?id=projects)

#### Examples
```python
import patch_api

patch = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))

# Retrieve a project
project_id = 'pro_test_1234' # Pass in the project's ID
patch.projects.retrieve_project(id=project_id)

# Retrieve a list of projects
page = 1 # Pass in which page of projects you'd like
patch.projects.retrieve_projects(page=page)
```

### Preferences
Preferences are how you route your orders in Patch. If you don't have a preference, Patch will allocate your order to the least expensive option. If you do have a preference, all of your orders will be sent to that project. You can set your preferences via API, or through the [Patch Dashboard](https://dashboard.usepatch.com/projects).

[API Reference](https://docs.usepatch.com/#/?id=preferences)

#### Examples
```python
import patch_api

patch = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))

# Create a preference

project_id = 'pro_test_1234' # Pass in the project_id for your preference
patch.preferences.create_preference(project_id=project_id)

# Retrieve a preference
preference_id = 'pre_test_1234' # Pass in the preferences's id
patch.preferences.retrieve_preference(preference_id=preference_id)

# Delete a preference
preference_id = 'pre_test_1234' # Pass in the preferences's id
patch.preferences.delete_preference(preference_id=preference_id)

# Retrieve a list of preferences
page = 1 # Pass in which page of preferences you'd like
patch.preferences.retrieve_preferences(page=page)
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

patch = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
orders = patch.orders.retrieve_orders(page=1)

print(orders)
```
