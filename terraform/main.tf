provider "google" {
  project = var.project
  region  = "europe-west1"
  zone    = "europe-west1-b"
}

resource "google_compute_instance" "lora_trainer" {
  name         = "lora-trainer"
  machine_type = "n1-standard-4"
  zone         = "europe-west1-b"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata_startup_script = <<-EOT
    #!/bin/bash
    echo "Starting LoRA training setup..."
    # Add your startup commands here
  EOT
}
