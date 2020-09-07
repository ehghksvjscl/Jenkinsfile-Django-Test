pipeline {
    environment {
        registry = "ehghksvjscl/django-jenkins"
	localregistry = "localhost:5000/django-jenkins"
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
        stage('Deploy docker image to real_docker registry') {
            steps {
                withDockerRegistry([ credentialsId: registryCredential, url: "" ]) {
                    sh 'docker push $registry:latest'
                }
            }
        }
	stage('Deploy docker image to local_docker registry') {
	    steps {
		sh 'docker tag $registry $localregistry'
		sh 'docker push $localregistry:latest'
	    }	
	}
        stage('Clean docker image - real docker reg') {
            steps{
		sh "docker rmi $registry:latest"
            }
        }

	stage('Clean docker image python - local docker reg') {
	    steps{
	        sh "docker rmi $rmipython"
	    }
	}
        stage('Clean docker image Django - local docker reg') {
            steps{
                sh "docker rmi $localregistry"
            }
        }

     }
}

