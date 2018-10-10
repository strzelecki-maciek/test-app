provider "google" {
  credentials = "${file("~/key.json")}"
  project     = "macieks-funland"
  region      = "eu-west-1"
}
