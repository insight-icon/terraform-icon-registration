output "public_ip" {
  value = var.public_ip
}

output "details_endpoint" {
  value = local.details_endpoint
}

output "details_content" {
  value = template_file.details.rendered
}

output "registration_json" {
  value = template_file.registration.rendered
}

output "network_name" {
  value = var.network_name
}

output "operator_password" {
  value = join("", data.external.preptools[0].result.*.operator_keystore_password)
}

output "operator_wallet_path" {
  value = join("", data.external.preptools[0].result.*.operator_keystore_path)
}

output "url" {
  value = local.url
}

output "nid" {
  value = local.nid
}