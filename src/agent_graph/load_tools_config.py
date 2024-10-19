
import os
import yaml
from dotenv import load_dotenv
from pyprojroot import here

load_dotenv()


class LoadToolsConfig:

    def __init__(self) -> None:
        with open(here("configs/tools_config.yml")) as cfg:
            app_config = yaml.load(cfg, Loader=yaml.FullLoader)

        # Set environment variables
        os.environ['OPENAI_API_KEY'] = os.getenv("OPEN_AI_API_KEY")
       

        # Primary agent
        self.primary_agent_llm = app_config["primary_agent"]["llm"]
        self.primary_agent_llm_temperature = app_config["primary_agent"]["llm_temperature"]

     

        # Swiss Airline Policy RAG configs
        self.policy_rag_llm = app_config["normativa_policy_rag"]["llm"]
        self.policy_rag_llm_temperature = float(
            app_config["normativa_policy_rag"]["llm_temperature"])
        self.policy_rag_embedding_model = app_config["normativa_policy_rag"]["embedding_model"]
        self.policy_rag_vectordb_directory = str(here(
            app_config["normativa_policy_rag"]["vectordb"]))  # needs to be strin for summation in chromadb backend: self._settings.require("persist_directory") + "/chroma.sqlite3"
        self.policy_rag_unstructured_docs_directory = str(here(
            app_config["normativa_policy_rag"]["unstructured_docs"]))
        self.policy_rag_k = app_config["normativa_policy_rag"]["k"]
        self.policy_rag_chunk_size = app_config["normativa_policy_rag"]["chunk_size"]
        self.policy_rag_chunk_overlap = app_config["normativa_policy_rag"]["chunk_overlap"]
        self.policy_rag_collection_name = app_config["normativa_policy_rag"]["collection_name"]

        # Stories RAG configs
        self.stories_rag_llm = app_config["seguros_rag"]["llm"]
        self.stories_rag_llm_temperature = float(
            app_config["seguros_rag"]["llm_temperature"])
        self.stories_rag_embedding_model = app_config["seguros_rag"]["embedding_model"]
        self.stories_rag_vectordb_directory = str(here(
            app_config["seguros_rag"]["vectordb"]))  # needs to be strin for summation in chromadb backend: self._settings.require("persist_directory") + "/chroma.sqlite3"
        self.stories_rag_unstructured_docs_directory = str(here(
            app_config["seguros_rag"]["unstructured_docs"]))
        self.stories_rag_k = app_config["seguros_rag"]["k"]
        self.stories_rag_chunk_size = app_config["seguros_rag"]["chunk_size"]
        self.stories_rag_chunk_overlap = app_config["seguros_rag"]["chunk_overlap"]
        self.stories_rag_collection_name = app_config["seguros_rag"]["collection_name"]

        # Siniestros SQL Agent configs
        self.travel_sqldb_directory = str(here(
            app_config["siniestros_procesados_sqlagent_configs"]["travel_sqldb_dir"]))
        self.travel_sqlagent_llm = app_config["siniestros_procesados_sqlagent_configs"]["llm"]
        self.travel_sqlagent_llm_temperature = float(
            app_config["siniestros_procesados_sqlagent_configs"]["llm_temperature"])

        

        # Graph configs
        self.thread_id = str(
            app_config["graph_configs"]["thread_id"])
