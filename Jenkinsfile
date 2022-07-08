// pipeline { 
//     agent { 
//         docker { image 'python:3.9.5' } 
//     } 
//     stages {
//         stage('Build') { 
//             steps { 
//                 echo 'test'
//                 script {
//                     sh "python -m unittest discover -v"
//                     sh "python --version"
//                 }
//             }
//         }   
//     }
// }
pipeline {
    agent {
        docker { image 'node:16.13.1-alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}