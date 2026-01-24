terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  project = "strategic-team-485314-k5"
  region  = "us-central1"
}

# 1. Google Cloud Storage Bucket (Data Lake)
resource "google_storage_bucket" "data-lake-bucket" {
  name          = "dtc_data_lake_strategic-team-485314-k5" # Unique bucket name
  location      = "US"

  # Optional settings for cost control
  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled     = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30  # Auto-delete files after 30 days
    }
  }

  force_destroy = true
}

# 2. BigQuery Dataset (Data Warehouse)
resource "google_bigquery_dataset" "dataset" {
  dataset_id = "trips_data_all"
  project    = "strategic-team-485314-k5"
  location   = "US"
}