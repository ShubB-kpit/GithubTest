pipeline {
    agent any
     
    stages {
        stage('Ok') {
            steps {
                echo "Ok"
            }
        }
        stage('build name') {
            steps {
                script {
                    def buildNumber = 0
                    echo buildNumber
                }
            }
        }
    }
    post {
        always {
            emailext body: 'testing',subject: 'testing', to: 'shubham.bawankar@kpit.com'
        }
    }
}
