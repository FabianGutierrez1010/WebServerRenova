pipeline { 
    agent any 
    stages {
        stage('Build') { 
            steps { 
                echo 'build'
                script {
                    bat "docker image build -t fabiangg/renova_cont:1.0.${BUILD_ID} ."
                }
            }
        }
        stage('Test'){
            steps {
                echo 'test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploy 2'
            }
        }
    }
}