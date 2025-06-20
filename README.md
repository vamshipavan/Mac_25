# uncertainty_clustering

Extract feature vectors from store analysis data files and generate picasso-ready annotation clusters.

## Instructions

### Step 1: Start Classification Server

Edit the `start_server.sh` file:

Set the appropriate model paths based on whether you're using POS or Product classification:

Example for POS:
```bash
LABELS_PATH="/disk/repository/classification-model/cls_itg_pos_combined.txt"
WEIGHT_PATH="/disk/repository/classification-model/cls_itg_pos_combined.pth.tar"

Then execute the shell script to start 4 model server instances:

./start_server.sh
```` 

Step 2: Edit Configuration

Edit example_config.yaml:

Ensure the endpoint matches the model configuration used in start_server.sh

Set values for the following fields:

    start_date

    end_date

    project_id

    exp_name

    endpoint (based on the cluster you are trying to create: POS or Product)
Run the clustering script with:

```bash
python main.py example_config.yaml
````
