resource "google_artifact_registry_repository" "chainlit_repo" {
  location = "us-central1"
  project  = "sacred-alliance-433217-e3"
  repository_id = "chainlit-repo"
  description = "chainlit Repository"
  format = "DOCKER"
}