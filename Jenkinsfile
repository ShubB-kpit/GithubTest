pipeline {
    agent any
     
    stages {
        stage('Ok') {
            steps {
                echo "Ok"
            }
        }
    }
    post {
        always {
            mail to: shubham.bawankar@kpit.com, subject: 'The Pipeline failed :('

        }
    }
}
