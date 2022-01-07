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
            mail to: shubham.bawankar@kpit.com, subject: 'The Pipeline failed :('

        }
    }
}
