
variable "skip_registration" {
  description = "Boolean to skip executing registration command"
  type        = bool
  default     = false
}

variable "static_endpoint" {
  description = "Endpoint to host static content"
  type        = string
}

########
# Label
########
variable "environment" {
  description = "The environment"
  type        = string
  default     = "dev"
}

variable "namespace" {
  description = "The namespace to deploy into"
  type        = string
  default     = "icon"
}

variable "stage" {
  description = "The stage of the deployment"
  type        = string
  default     = "blue"
}

variable "network_name" {
  description = "mainnet or testnet - Don't mess this up!!!!!!!!"
  type        = string
  default     = "mainnet"
}

variable "owner" {
  description = "Owner of the infrastructure"
  type        = string
  default     = "insight"
}

// ------------------Registration

variable "organization_name" {
  description = "Any string - your team name"
  type        = string
  default     = ""
}
variable "organization_country" {
  description = "This needs to be three letter country code per https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3"
  type        = string
  default     = ""
}
variable "organization_email" {
  description = "Needs to be real email"
  type        = string
  default     = ""
}
variable "organization_city" {
  description = "No qualifiers"
  type        = string
  default     = ""
}
variable "organization_website" {
  description = "Needs to begin in https / http - can be google..."
  type        = string
  default     = ""
}

// ------------------Details

variable "logo_256" {
  description = "Path to png logo"
  type        = string
  default     = ""
}
variable "logo_1024" {
  description = "Path to png logo"
  type        = string
  default     = ""
}
variable "logo_svg" {
  description = "Path to svg logo"
  type        = string
  default     = ""
}
variable "steemit" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "twitter" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "youtube" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "facebook" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "github" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "reddit" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "keybase" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "telegram" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "wechat" {
  description = "Link to social media account - https://..."
  type        = string
  default     = ""
}
variable "server_type" {
  description = "Link to social media account - https://..."
  type        = string
  default     = "cloud"
}

variable "public_ip" {
  description = "Optional if you are registering an IP from a different network - only creates details content, leave blank and insert cloud provdier to create ip"
  type        = string
  default     = null
}

//------------------

variable "keystore_path" {
  description = "the path to your keystore"
  type        = string
}

variable "keystore_password" {
  description = "The keystore password"
  type        = string
}

variable "operator_keystore_password" {
  description = "the path to your keystore"
  type        = string
  default     = ""
}

variable "operator_keystore_path" {
  description = "The keystore password"
  type        = string
  default     = ""
}
