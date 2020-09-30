terraform {
  required_version = ">= 0.12"
}

resource "random_pet" "this" {
  length = 2
}

locals {
  nid_map = {
    mainnet = 1
    testnet = 2
    bicon   = 3
    zicon   = 80
  }

  url_map = {
    mainnet = "https://ctz.solidwallet.io"
    testnet = "https://test-ctz.solidwallet.io"
    bicon   = "https://bicon.net.solidwallet.io"
    zicon   = "https://zicon.net.solidwallet.io"
  }

  nid = local.nid_map[var.network_name]
  url = local.url_map[var.network_name]

  details_endpoint = "${var.static_endpoint}/details.json"
}

###########
# Templates
###########
resource template_file "details" {
  template = file("${path.module}/templates/details.json")
  vars = {
    logo_256  = var.logo_256 == "" ? "" : "${var.static_endpoint}/${basename(var.logo_256)}"
    logo_1024 = var.logo_1024 == "" ? "" : "${var.static_endpoint}/${basename(var.logo_1024)}"
    logo_svg  = var.logo_svg == "" ? "" : "${var.static_endpoint}/${basename(var.logo_svg)}"

    steemit  = var.steemit
    twitter  = var.twitter
    youtube  = var.youtube
    facebook = var.facebook
    github   = var.github
    reddit   = var.reddit
    keybase  = var.keybase
    telegram = var.telegram
    wechat   = var.wechat

    country     = var.organization_country
    region      = var.organization_city
    server_type = var.server_type

    public_ip = var.public_ip
  }
}

resource "template_file" "registration" {
  template = file("${path.module}/templates/registerPRep.json")
  vars = {
    name    = var.organization_name
    country = var.organization_country
    city    = var.organization_city
    email   = var.organization_email
    website = var.organization_website

    details_endpoint = local.details_endpoint

    public_ip = var.public_ip
  }
}

resource template_file "preptools_config" {
  template = file("${path.module}/templates/preptools_config.json")
  vars = {
    nid           = local.nid
    url           = local.url
    keystore_path = var.keystore_path
  }
}

#################
# Persist objects
#################
resource "local_file" "preptools_config" {
  filename = "${path.module}/preptools_config.json"
  content  = template_file.preptools_config.rendered
}

resource "local_file" "registerPRep" {
  filename = "${path.module}/registerPRep.json"
  content  = template_file.registration.rendered
}

###################
# Register / Update
###################

locals {
  operator_inputs = var.operator_keystore_password == "" ? {
    operator_keystore_password = var.operator_keystore_password
    operator_keystore_path     = var.operator_keystore_path
  } : {}
}

data "external" "preptools" {
  count   = var.skip_registration ? 0 : 1
  program = ["python3", "${path.module}/scripts/preptools_wrapper.py"]

  query = merge({
    network_name      = var.network_name,
    keystore_path     = var.keystore_path
    register_json     = local_file.registerPRep.filename,
    keystore_password = var.keystore_password
    url               = local.url
    nid               = local.nid
  }, local.operator_inputs)

  depends_on = [local_file.preptools_config, local_file.registerPRep]
}

