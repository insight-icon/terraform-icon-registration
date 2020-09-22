variable "logo_256" {
  default = ""
}

variable "logo_1024" {
  default = ""
}

variable "logo_svg" {
  default = ""
}

variable "keystore_path" {
  default = ""
}

variable "keystore_password" {
  default = "testing1."
}

locals {
  keystore_path = var.keystore_path == "" ? "${path.cwd}/../../test/fixtures/keystore/testnet" : var.keystore_path
  logo_256      = var.logo_256 == "" ? "${path.cwd}/../../test/fixtures/logos/insight.png" : var.logo_256
  logo_1024     = var.logo_1024 == "" ? "${path.cwd}/../../test/fixtures/logos/insight.png" : var.logo_1024
  logo_svg      = var.logo_svg == "" ? "${path.cwd}/../../test/fixtures/logos/insight.png" : var.logo_svg
}

module "defaults" {
  source = "../.."

  network_name = "zicon"

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

output "operator_wallet_path" {
  value = module.defaults.operator_wallet_path
}