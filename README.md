# terraform-aws-icon-registration

## Features

This module helps with registering a node on the ICON Blockchain. It is meant to be used by the following cloud specific 
registration modules:
- [terraform-icon-aws-registration]

- Creates an elastic IP that will be your main IP that your node will use to run and applies a number of tags on the
resource so it can be queried to be attached to instances later
- Puts the necessary details.json file in a bucket publicly accessible along with logos
- Runs `preptools` to register the node or update the info

**Make sure you have 2000 ICX registration fee in your wallet for mainnet and you have testnet tokens for testnet**

## Using this module

Fill out the appropriate values in `terraform.tfvars.example` then move to `terraform.tfvars` if running directly.

Really this module should be used from a scaffolding like `terragrunt` like in (terragrunt-aws-icon)[https://github.com/insight-infrastructure/terragrunt-aws-icon]

## Terraform Versions

For Terraform v0.12.0+

## Usage

```hcl
module "this" {
    source = "github.com/insight-infrastructure/terraform-aws-icon-registration.git?ref=v0.1.0"
    network_name = "testnet"

    // Path needs to be filled in otherwise registration doesn't work
    //  keystore_path = "/Users/.../Documents/keystore"

    organization_name    = "Insight-CI"
    organization_country = "USA"
    # This needs to be three letter country code per https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
    organization_email = "hunter@gmail.com"
    # Needs to be real email
    organization_city = "A city"
    # No qualifiers
    organization_website = "https://google.com"
    # Needs to begin in https / http - can be google...

    // All the logos are complete paths to the image on your local drive
    logo_256 = "/Users/.../logo_256"
    logo_1024 = "/Users/.../logo_1024"
    logo_svg = "/Users/.../logo_svg"

    // If you have already have an IP, you can enter it here / uncomment and a new IP will not be provisioned with the
    // existing IP being brought
    //  ip = "1.2.3.4"
    // ------------------Details - Doesn't really matter
    server_type = "cloud"
    region      = "us-east-1"

    keystore_password = var.keystore_password
    keystore_path     = var.keystore_path

    logo_256  = var.logo_256
    logo_1024 = var.logo_1024

    logo_svg = var.logo_svg
}
```

## Examples

- [defaults](https://github.com/robc-io/terraform-aws-icon-registration/tree/master/examples/defaults)

## Known  Issues
No issue is creating limit on this module.

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Providers

| Name | Version |
|------|---------|
| local | n/a |
| null | n/a |
| random | n/a |
| template | n/a |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:-----:|
| environment | The environment | `string` | `"dev"` | no |
| facebook | Link to social media account - https://... | `string` | `""` | no |
| github | Link to social media account - https://... | `string` | `""` | no |
| keybase | Link to social media account - https://... | `string` | `""` | no |
| keystore\_password | The keystore password | `string` | n/a | yes |
| keystore\_path | the path to your keystore | `string` | n/a | yes |
| logo\_1024 | Path to png logo | `string` | `""` | no |
| logo\_256 | Path to png logo | `string` | `""` | no |
| logo\_svg | Path to svg logo | `string` | `""` | no |
| namespace | The namespace to deploy into | `string` | `"icon"` | no |
| network\_name | mainnet or testnet - Don't mess this up!!!!!!!! | `string` | `"mainnet"` | no |
| organization\_city | No qualifiers | `string` | `""` | no |
| organization\_country | This needs to be three letter country code per https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3 | `string` | `""` | no |
| organization\_email | Needs to be real email | `string` | `""` | no |
| organization\_name | Any string - your team name | `string` | `""` | no |
| organization\_website | Needs to begin in https / http - can be google... | `string` | `""` | no |
| owner | Owner of the infrastructure | `string` | `"insight"` | no |
| packet\_project\_name | The project name for packet | `string` | `""` | no |
| public\_ip | Optional if you are registering an IP from a different network - only creates details content, leave blank and insert cloud provdier to create ip | `string` | n/a | yes |
| reddit | Link to social media account - https://... | `string` | `""` | no |
| server\_type | Link to social media account - https://... | `string` | `"cloud"` | no |
| stage | The stage of the deployment | `string` | `"blue"` | no |
| static\_endpoint | Endpoint to host static content | `string` | n/a | yes |
| steemit | Link to social media account - https://... | `string` | `""` | no |
| telegram | Link to social media account - https://... | `string` | `""` | no |
| twitter | Link to social media account - https://... | `string` | `""` | no |
| wechat | Link to social media account - https://... | `string` | `""` | no |
| youtube | Link to social media account - https://... | `string` | `""` | no |

## Outputs

| Name | Description |
|------|-------------|
| details\_endpoint | n/a |
| details\_values | n/a |
| network\_name | n/a |
| public\_ip | n/a |
| registration\_command | n/a |
| registration\_json | n/a |
| update\_registration\_command | n/a |

<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->

## Testing
This module has been packaged with terratest tests

To run them:

1. Install Go
2. Run `make test-init` from the root of this repo
3. Run `make test` again from root

## Authors

Module managed by [robc-io](github.com/robc-io)

## Credits

- [Anton Babenko](https://github.com/antonbabenko)

## License

Apache 2 Licensed. See LICENSE for full details.