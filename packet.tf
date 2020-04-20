variable "packet_project_name" {
  description = "The project name for packet"
  type        = string
  default     = ""
}

//resource "packet_project" "this" {
//  count = var.cloud_provider == "packet" ? 1 : 0
//
//  name = var.packet_project_name
//}
//
//resource "packet_reserved_ip_block" "test" {
//  count = var.cloud_provider == "packet" ? 1 : 0
//
//  project_id = join("", packet_project.this.*.id)
//  type       = "global_ipv4"
//  quantity   = 1
//}

