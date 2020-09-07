pipeline {
    environment {
        registry = "ehghksvjscl/django-jenkins"
        registryCredential = 'docker_id'
	rmipython = 'python:3'
	localhost = 'localhost:5000'
    }
    agent any
    stages {
	stage('UnitTest Django') {
	    steps {
	    	sh 'python3 manage.py test'
	    }
	}
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
		sh "docker rmi $rmipython"
            }
        }
     }
}

