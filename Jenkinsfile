def lastSuccessBuildName = ""

pipeline {
    agent any
    stages {
        stage('Welcome Step') {
            steps { 
                script {
                    echo 'Welcome to the LambdaTest'
                    lastSuccessBuildName = Jenkins.instance.getItemByFullName('multiP/branch2').getLastSuccessfulBuild().getAbsoluteUrl()
                    echo "last Success Build Name: ${lastSuccessBuildName}"
                }
            }
        }
        stage('check if py file exists'){
            steps {
                
                script {
                    if(fileExists("./pyFilesForShpt/getEmailText.py")) {
                        echo 'py file exists'
                        var1 = bat(script:'python ./pyFilesForShpt/getEmailText.py \${lastSuccessBuildName} arg2 arg3', returnStdout: true).trim()
                        echo "got var1"
                        var2 = var1[var1.indexOf('<html>')..(var1.indexOf('</html>')+6)]
                        echo "got var2"
                        writeFile file: 'smpl.txt', text: var2
                        echo "got smpl.txt"
                        mail to:'shubham.bawankar@kpit.com',
                        mimeType: 'text/html',
                        subject:'load2Sharepoint_test',
                        body: var2   
                    }
                    else {
                        echo '404: file not exists'
                    }
                }
                
            }
            
        }
    }
}
