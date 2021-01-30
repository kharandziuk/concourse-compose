from invoke import task

CI_NAME = 'concourse-compose'

PIPELINE_NAME = 'manual'

@task
def concourse_login(c):
    c.run(f'fly login -t {CI_NAME} -u test -p test -c http://localhost:8080')


@task(concourse_login)
def set_pipelines(c):
    c.run(f'fly -t {CI_NAME} set-pipeline -c pipeline.yml -p {PIPELINE_NAME}')

@task
def unpause(c):
    c.run(f'fly -t {CI_NAME} unpause-job --job {PIPELINE_NAME}/integration')


@task
def trigger(c):
    c.run(f'fly -t {CI_NAME} trigger-job --job {PIPELINE_NAME}/integration')
