# terraform-icon-registration

## Features

This module helps with registering a node on the ICON Blockchain. It is meant to be used by the following cloud specific 
registration modules:

- [terraform-icon-aws-registration](https://github.com/insight-icon/terraform-icon-aws-registration)
- [terraform-icon-gcp-registration](https://github.com/insight-icon/terraform-icon-gcp-registration)
- [terraform-icon-azure-registration](https://github.com/insight-icon/terraform-icon-azure-registration) - WIP
- [terraform-icon-aws-registration](https://github.com/insight-icon/terraform-icon-gcp-registration) - WIP
- [terraform-icon-packet-registration](https://github.com/insight-icon/terraform-icon-packet-registration) - WIP 
- [terraform-icon-hetzner-registration](https://github.com/insight-icon/terraform-icon-hetzner-registration) - WIP 

These modules then do the following:
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
  source = "../.."

  network_name = "testnet"

  public_ip       = "1.2.3.4"
  static_endpoint = "https://google.com"

  organization_name    = "Insight-CI"
  organization_country = "USA"
  organization_email   = "hunter@gmail.com"
  organization_city    = "A city"
  organization_website = "https://google.com"
  server_type          = "cloud"

  keystore_password = var.keystore_password
  keystore_path     = local.keystore_path

  logo_256  = local.logo_256
  logo_1024 = local.logo_1024
  logo_svg  = local.logo_svg
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
| external | n/a |
| local | n/a |
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
| operator\_keystore\_password | the path to your keystore | `string` | `""` | no |
| operator\_keystore\_path | The keystore password | `string` | `""` | no |
| organization\_city | No qualifiers | `string` | `""` | no |
| organization\_country | This needs to be three letter country code per https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3 | `string` | `""` | no |
| organization\_email | Needs to be real email | `string` | `""` | no |
| organization\_name | Any string - your team name | `string` | `""` | no |
| organization\_website | Needs to begin in https / http - can be google... | `string` | `""` | no |
| owner | Owner of the infrastructure | `string` | `"insight"` | no |
| public\_ip | Optional if you are registering an IP from a different network - only creates details content, leave blank and insert cloud provdier to create ip | `string` | n/a | yes |
| reddit | Link to social media account - https://... | `string` | `""` | no |
| server\_type | Link to social media account - https://... | `string` | `"cloud"` | no |
| skip\_registration | Boolean to skip executing registration command | `bool` | `false` | no |
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
| details\_content | n/a |
| details\_endpoint | n/a |
| network\_name | n/a |
| nid | n/a |
| operator\_password | n/a |
| operator\_wallet\_path | n/a |
| public\_ip | n/a |
| registration\_json | n/a |
| url | n/a |

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