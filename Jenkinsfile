pipeline {
    agent any

    parameters {
        string(name: 'URL1', defaultValue: 'https://raw.githubusercontent.com/ALEXNETHUNTER/Python/main/1st.json', description: 'URL to the first JSON file')
        string(name: 'URL2', defaultValue: 'https://raw.githubusercontent.com/ALEXNETHUNTER/Python/main/2nd.json', description: 'URL to the second JSON file')
        string(name: 'GIT_URL', defaultValue: 'https://github.com/ALEXNETHUNTER/Python.git', description: 'Git repository URL')
        string(name: 'GIT_BRANCH', defaultValue: 'main', description: 'Git branch name')
        string(name: 'GIT_CREDENTIALS_ID', defaultValue: 'my-git-credentials-id', description: 'Jenkins credentials ID for Git')
    }

    environment {
        gitlabSourceBranch = 'main'
        GIT_AUTHOR_EMAIL = 'alexnethunter@gmail.com'
        GIT_AUTHOR_NAME = 'alexnethunter'
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

        stage('Install Python Req.') {
            steps {
                sh 'sudo apt install python3-pip'
                sh 'python3 -m pip install requests'
            }
        }

        stage('Checkout') {
            steps {
                git credentialsId: params.GIT_CREDENTIALS_ID, url: params.GIT_URL, branch: params.GIT_BRANCH
            }
        }

        stage('Fetch & Merge JSONs') {
            steps {
                script {
                    try {
                        sh "python3 json_merge.py ${params.URL1} ${params.URL2}"
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
                script {
                    try {
                            sh '''
                                git config --global credential.helper store
                                git remote set-url origin https://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@github.com/ALEXNETHUNTER/Python.git
                                git config --global user.email "${GIT_AUTHOR_EMAIL}"
                                git config --global user.name "${GIT_AUTHOR_NAME}"
                                git add merged_output.json
                                git commit -m "Automatically committed merged JSON output" || echo "Nothing to commit"
                                git push -u origin ${GIT_BRANCH} || echo "Nothing to push"
                            '''
                    } catch (Exception e) {
                        echo "Failed to push to Git repository: ${e.message}"
                        currentBuild.result = 'FAILURE'
                        error("${e.message}")
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
