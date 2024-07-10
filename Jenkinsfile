pipeline {
    agent any
    
    parameters {
        string(name: 'URL1', description: 'URL to the first JSON file')
        string(name: 'URL2', description: 'URL to the second JSON file')
    }
    
    options {
        disableConcurrentBuilds()
        timestamps()
    }
    
    stages {
        stage("Add a description for the build") {
            steps {
                script {
                    currentBuild.displayName = "Operate JSON files using a Python"
                    currentBuild.description = "Operate JSON files using a Python description"
                }
            }
        }

        stage('Checkout source from repo') {
            steps {
                git 'https://github.com/ALEXNETHUNTER/Python.git'
            }
        }
        
        stage('Fetch & Merge JSONs') {
            steps {
                script {
                    try {
                        sh "python merge_jsons.py ${params.URL1} ${params.URL2}"
                    } catch (Exception e) {
                        echo "Failed to fetch and merge JSON files: ${e.message}"
                        currentBuild.result = 'FAILURE'
                        error("${e.message}")
                    }
                }
            }
        }
        
        stage('Commit Output') {
            steps {
                withCredentials([usernamePassword(git branch: 'main', credentialsId: 'my-git-credentials-id', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                script {
                    try {
                        gitAdd()
                        gitCommit(message: 'Automated commit: merged JSON files')
                        gitPush()
                    } catch (Exception e) {
                        echo "Failed to commit and push merged output: ${e.message}"
                        currentBuild.result = 'FAILURE'
                        error("${e.message}")
                    }
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed :('
        }
    }
}
