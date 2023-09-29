from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "fraud-deneme-0929084745",
}

dag = DAG(
    "fraud-deneme-0929084745",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `fraud-deneme.py`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: fraud-deneme.py

op_c4919e9e_7b4e_4607_8a93_c6c84c4747ec = KubernetesPodOperator(
    name="fraud_deneme",
    namespace="default",
    image="quay.io/opendatahub-contrib/runtime-images:spark-ubi9-py39_2023b_latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'fraud-deneme' --cos-endpoint http://minio-dspipeline.kubeflow.svc.cluster.local:9000 --cos-bucket default --cos-directory 'fraud-deneme-0929084745' --cos-dependencies-archive 'fraud-deneme-c4919e9e-7b4e-4607-8a93-c6c84c4747ec.tar.gz' --file 'fraud-deneme.py' "
    ],
    task_id="fraud_deneme",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "3Oy7ju3JZiYAcx8T",
        "AWS_SECRET_ACCESS_KEY": "p7cDsD3Fnk4TZF3qjQQB7eLX",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fraud-deneme-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)
