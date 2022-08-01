ARG BASE=${BASE:-openkbs/python-nonroot-docker}
FROM ${BASE}

MAINTAINER DrSnowbird "DrSnowbird@openkbs.org"

###############################
#### ---- App: (ENV)  ---- ####
###############################
USER ${USER:-developer}
WORKDIR ${HOME:-/home/developer}

ENV APP_HOME=${APP_HOME:-$HOME/app}
ENV APP_MAIN=${APP_MAIN:-setup.sh}

#################################
#### ---- App: (common) ---- ####
#################################
WORKDIR ${APP_HOME}
RUN python -u -m pip install --upgrade pip

###############################
#### ---- App Setup:  ---- ####
###############################
RUN sudo chown -R ${USER}:${USER} ${APP_HOME} && \
    git clone https://files.caseontology.org/git/CASE-Workshop-2022-08-01.git ${APP_HOME}

COPY --chown=$USER:$USER ./bin $HOME/bin

#RUN $HOME/bin/pre-load-virtualenv.sh && \

RUN if [ -s ${APP_HOME}/requirements.txt ]; then \
        pip install --no-cache-dir --user -r ${APP_HOME}/requirements.txt ; \
    fi; 
 
ENV PATH=${HOME}/.local/bin:${PATH}
    
#########################################
##### ---- Setup: Entry Files  ---- #####
#########################################
COPY --chown=${USER}:${USER} docker-entrypoint.sh /
COPY --chown=${USER}:${USER} ${APP_MAIN} ${APP_HOME}/setup.sh

RUN sudo chown -R ${USER}:${USER} ${APP_HOME} && \
    sudo chmod +x /docker-entrypoint.sh ${APP_HOME}/setup.sh 

#########################################
##### ---- Docker Entrypoint : ---- #####
#########################################
ENTRYPOINT ["/docker-entrypoint.sh"]

#####################################
##### ---- user: developer ---- #####
#####################################
WORKDIR ${APP_HOME}
USER ${USER}

#############################################
#############################################
#### ---- App: (Customization here) ---- ####
#############################################
#############################################
#### (you customization code here!) #########
COPY --chown=$USER:$USER  ./app $HOME/app
#RUN git clone https://github.com/casework/CASE-Mapping-Template-Python && \
#    wget https://files.caseonotlogy.org/CASE-Corpora/govdocs1/000/000015.pdf && \
#    wget https://files.caseonotlogy.org/CASE-Corpora/govdocs1/000/000015.pdf.pdfinfo.txt && \
#    wget https://files.caseonotlogy.org/CASE-Corpora/govdocs1/000/000015.pdf.pdfinfo-jsondates.txt
    

######################
#### (Test only) #####
######################
#CMD ["/bin/bash"]
######################
#### (RUN setup) #####
######################
#CMD ["setup.sh"]
CMD ["/bin/bash"]
