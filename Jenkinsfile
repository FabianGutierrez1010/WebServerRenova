pipeline { 
    agent any
    stages {
        stage('Build') { 
            steps { 
                echo 'build'
                script {
                    bat "docker build -f dockerfile -t fabiangg/renova_cont:1.0.${BUILD_ID} ."
                    bat "docker build -f unittest.dockerfile -t fabiangg/test:1.0.${BUILD_ID} ."
                }
            }
        }
        stage('Test') { 
            steps { 
                echo 'run container test'
                script {
                    bat "docker run --name renovaTest${BUILD_ID} fabiangg/test:1.0.${BUILD_ID}"
                    // bat "docker exec -i renova${BUILD_ID} /bin/sh"
                    // echo 'version dentro del container'
                    // bat "docker exec --workdir /app renova${BUILD_ID} python --version"
                    // bat "docker exec --workdir /app renova${BUILD_ID} python -m unittest discover -v"
                    // echo 'version fuera del container'
                    // bat "python --version"
                    // bat "dir"
                    // sh "python -m unittest discover -v"
                    // sh "exit"
                }
            }
        }
        stage('Deploy') { 
            steps { 
                echo 'deploy'
                script {
                bat "docker run --name renova${BUILD_ID} -p 5050:5000 -d fabiangg/renova_cont:1.0.${BUILD_ID}"
                }
            }   
        }
    }
}
