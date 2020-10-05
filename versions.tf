terraform {
  required_providers {
    external = {
      source = "hashicorp/external"
    }
    local = {
      source = "hashicorp/local"
    }
    template = {
      source = "hashicorp/template"
    }
  }
  required_version = ">= 0.12"
}
