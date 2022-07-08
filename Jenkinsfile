pipeline { 
    agent any
    stages {
        stage('Build') { 
            steps { 
                echo 'build'
                script {
                    bat "docker build -t fabiangg/renova_cont:1.0.${BUILD_ID} ."
                }
            }
        }   
    }
    stages {
        stage('Test') { 
            steps { 
                echo 'try enter the container'
                script {
                    bat "docker run -p 5050:5000 -d fabiangg/renova_cont:1.0.${BUILD_ID}"
                    bat "docker exec -i -t a8af636ada32 /bin/sh"
                    sh "python -m unittest discover -v"
                    sh "exit"
                }
            }
        }
        stage('Deploy') { 
            steps { 
                echo 'test'
            }
        } 
    }
}
