# Patch Python SDK

![Test](https://github.com/patch-technology/patch-python/workflows/Test/badge.svg)
[![PyPI version](https://badge.fury.io/py/patch-api.svg)](https://badge.fury.io/py/patch-api)
[![Discord](https://img.shields.io/discord/733029448558837792)](https://discord.gg/AU8543D)

The official Python library for the [Patch API](https://www.patch.io).

## Documentation

For a complete API reference, check out [Patch's API Reference.](https://docs.patch.io/).

## Installation

Add the library to your `requirements.txt` file:

```txt
patch_api >= 1.5.0
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

- Python 3.6.1

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
patch.estimates.create_mass_estimate(mass_g=mass_g)

## You can also specify a project-id field (optional) to be used instead of the preferred one
project_id = 'pro_test_1234' # Pass in the project's ID
patch.estimates.create_mass_estimate(mass_g=mass_g, project_id=project_id)

# Create a flight estimate
distance_m = 1_000_000 # Pass in the distance traveled in meters
patch.estimates.create_mass_estimate(distance_m=distance_m)

# Create a shipping estimate
distance_m = 1_000_000 # Pass in the distance traveled in meters
transportation_method = "rail"
package_mass_g = 5000
patch.estimates.create_mass_estimate(distance_m=distance_m, transportation_method=transportation_method, package_mass_g=package_mass_g)

# Create a vehicle estimate
distance_m = 1_000_000 # Pass in the distance traveled in meters
make = "Toyota"
model = "Corolla"
year = 1995
patch.estimates.create_mass_estimate(distance_m=distance_m, make=make, model=model, year=year)

# Create a bitcoin estimate
transaction_value_btc_sats = 1000 # [Optional] Pass in the transaction value in satoshis
patch.estimates.create_bitcoin_estimate(transaction_value_btc_sats=transaction_value_btc_sats)

# Retrieve an estimate
estimate_id = 'est_test_1234'
patch.estimates.retrieve_estimate(id=estimate_id)

# Retrieve a list of estimates
page = 1 # Pass in which page of estimates you'd like
patch.estimates.retrieve_estimates(page=page)
```

### Projects

Projects are the ways Patch takes CO2 out of the air. They can represent reforestation, enhanced weathering, direct air carbon capture, etc. When you place an order via Patch, it is allocated to a project.

When fetching projects, you can supply filters to the query to narrow your result. Currently supported filters are:

- `country`
- `type`
- `minimum_available_mass`

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

# Retrieve a list of biomass projects
patch.projects.retrieve_projects(type="biomass")

# Retrieve a list of projects from Canada
patch.projects.retrieve_projects(country="CA")

# Retrieve a list of projects with at least 100 grams of available offsets
patch.projects.retrieve_projects(minimum_available_mass=100)
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

## Contributing

While we value open-source contributions to this SDK, the core of this library is generated programmatically. Complex additions made directly to the library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README, as well as new test cases are always very welcome!

### Pre-commit

This project uses pre-commit to automatically lint code on commit. Set-up lint commit the first time around using
```
pre-commit install
```

### Linter

This project uses black for code formatting. To run the automatic formatting, run:

```bash
make lint
```

### Running tests

Set up the required environment variable:

```bash
export SANDBOX_API_KEY=<SANDBOX API KEY>
```

Run tests:

```bash
make test
```

To run an individual test:

```bash
python -m unittest test/xxx_test.py
```

### Testing the built package locally

To build the library locally, run:

```bash
make build
```

In another directory, create a file called `patch.py` and install the local package in this directory:

```bash
touch patch.py
pip install ../patch-python
```

Set up the required environment variable:

```bash
export SANDBOX_API_KEY=<SANDBOX API KEY>
```

To test the package locally, create a python file in a sibling directory and add the following:

```python
import os
import patch_api

patch = patch_api.ApiClient(api_key=os.environ.get('SANDBOX_API_KEY'))
orders = patch.orders.retrieve_orders(page=1)

print(orders)
```
