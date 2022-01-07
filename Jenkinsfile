pipeline {
    agent any
     
    stages {
        stage('Ok') {
            steps {
                echo "Ok"
            }
        stage('build name') {
            steps {
                def buildNumber = Jenkins.instance.getItem('multiP').getItem('branch2').lastSuccessfulBuild.number
                echo buildNumber
            }
        }
    }
    post {
        always {
            emailext body: 'testing',subject: 'testing', to: 'shubham.bawankar@kpit.com'
        }
    }
}
