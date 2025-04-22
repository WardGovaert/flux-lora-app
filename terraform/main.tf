provider "google" {
  project = "pure-courier-453515-t8"
  region  = "europe-west1"
}

resource "google_compute_instance" "trainer" {
  name         = "lora-trainer"
  machine_type = "n1-standard-8"
  zone         = "europe-west1-a"

  boot_disk {
    initialize_params { image = "ubuntu-2004-focal" }
  }

  guest_accelerator {
    type  = "nvidia-tesla-t4"
    count = 1
  }

  metadata = { 
    startup-script = <<-EOT
      #!/bin/bash
      apt-get update
      apt-get install -y docker.io
      docker run -d -p 8000:8000 your-docker-image
    EOT
  }

  service_account {
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}