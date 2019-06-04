pipeline {

  agent any

    stages {
      stage('Deploy in cloud') {
        steps('Make and push docker image') {
          sh 'docker build -t tesqos/demojd .'
          sh 'docker push tesqos/demojd'
        }
      }

      stage('Deploy locally'){
        steps('Install in pip repository') {
          sh 'python setup.py sdist'
          sh 'pip install dist/*'
        }
      }

    }
}
