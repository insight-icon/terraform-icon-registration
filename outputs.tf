output "public_ip" {
  value = var.public_ip
}

output "details_endpoint" {
  value = local.details_endpoint
}

output "details_values" {
  value = template_file.details.rendered
}

output "registration_json" {
  value = template_file.registration.rendered
}

output "network_name" {
  value = var.network_name
}

output "registration_command" {
  value = <<-EOF
preptools registerPRep \
--url ${local.url} \
--nid ${local.nid} \
%{if var.keystore_path != ""}--keystore ${var.keystore_path}%{endif} \
%{if var.organization_name != ""}--name "${var.organization_name}"%{endif} \
%{if var.organization_country != ""}--country "${var.organization_country}"%{endif} \
%{if var.organization_city != ""}--city "${var.organization_city}"%{endif} \
%{if var.organization_email != ""}--email "${var.organization_email}"%{endif} \
%{if var.organization_website != ""}--website "${var.organization_website}"%{endif} \
--details "${local.details_endpoint}" \
--p2p-endpoint "${var.public_ip}:7100"
EOF
}

output "update_registration_command" {
  value = <<-EOF
preptools setPRep \
--url ${local.url} \
--nid ${local.nid} \
%{if var.keystore_path != ""}--keystore ${var.keystore_path}%{endif} \
%{if var.organization_name != ""}--name "${var.organization_name}"%{endif} \
%{if var.organization_country != ""}--country "${var.organization_country}"%{endif} \
%{if var.organization_city != ""}--city "${var.organization_city}"%{endif} \
%{if var.organization_email != ""}--email "${var.organization_email}"%{endif} \
%{if var.organization_website != ""}--website "${var.organization_website}"%{endif} \
--details "${local.details_endpoint}" \
--p2p-endpoint "${var.public_ip}:7100"
EOF
}