pipeline { 
    agent any 
    stages {
        stage('Build') { 
            steps { 
                echo 'test'
                script {
                    bat "py -m unittest discover -v"
                }
            }
        }   
    }
}