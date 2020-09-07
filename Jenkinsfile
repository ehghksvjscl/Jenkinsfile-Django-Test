pipeline {
    environment {
        registry = "ehghksvjscl/myapp-jenkins"
        registryCredential = 'docker_id'
    }
    agent any
    stages {
        stage('Build docker image') {
            steps {
                sh 'docker build -t $registry:latest .'
            }
        }
        stage('Deploy docker image') {
            steps {
                withDockerRegistry([ credentialsId: registryCredential, url: "" ]) {
                    sh 'docker push $registry:latest'
                }
            }
        }
        stage('Clean docker image') {
            steps{
                sh "docker rmi $registry"
            }
        }
     }
}

