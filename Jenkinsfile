pipeline { 
    agent { 
        docker { image 'python:3.9.5' } 
    } 
    stages {
        stage('Build') { 
            steps { 
                echo 'test'
                script {
                    sh "python -m unittest discover -v"
                    sh "python --version"
                }
            }
        }   
    }
}