# SK Assistants API DEMO

これは Semantic Kernel を用いて、簡単に Azure OpenAI Assistants API に接続するデモです。

## response image

```json
{
  "inner_content": null,
  "ai_model_id": null,
  "metadata": {},
  "content_type": "message",
  "role": "assistant",
  "name": "FileManipulation",
  "items": [
    {
      "inner_content": null,
      "ai_model_id": null,
      "metadata": {},
      "content_type": "text",
      "text": "# Let's first read the contents of the uploaded file to understand its structure and extract relevant information.\r\nfile_path = '/mnt/data/assistant-pW3CLB3GWbkQworP4Rt8FsdO'\r\n\r\n# Open and read the file\r\nwith open(file_path, 'r') as file:\r\n    content = file.read()\r\n\r\ncontent[:1000]  # Displaying first 1000 characters for an overview, to understand its structure.",
      "encoding": null
    }
  ],
  "encoding": null,
  "finish_reason": null
}
```

```json
{
  "inner_content": null,
  "ai_model_id": null,
  "metadata": {},
  "content_type": "message",
  "role": "assistant",
  "name": "FileManipulation",
  "items": [
    {
      "inner_content": null,
      "ai_model_id": null,
      "metadata": {},
      "content_type": "text",
      "text": "import pandas as pd\r\nfrom io import StringIO\r\n\r\n# Load the CSV data into a DataFrame\r\ndata = StringIO(content)\r\ndf = pd.read_csv(data)\r\n\r\n# Display the first few rows of the dataframe to ensure it loaded correctly\r\ndf.head()",
      "encoding": null
    }
  ],
  "encoding": null,
  "finish_reason": null
}
```

```json
{
  "inner_content": null,
  "ai_model_id": null,
  "metadata": {},
  "content_type": "message",
  "role": "assistant",
  "name": "FileManipulation",
  "items": [
    {
      "inner_content": null,
      "ai_model_id": null,
      "metadata": {},
      "content_type": "text",
      "text": "The file appears to be in CSV format with the following columns:\n\n- **category**\n- **product_name**\n- **dates**\n- **quantities**\n- **sales_totals**\n- **profits_totals**\n- **weather_conditions**\n\nTo identify which category had the most sales, I'll extract the relevant data and compute the total sales for each category. Let's proceed with that calculation.",
      "encoding": null
    }
  ],
  "encoding": null,
  "finish_reason": null
}
```

```json
{
  "inner_content": null,
  "ai_model_id": null,
  "metadata": {},
  "content_type": "message",
  "role": "assistant",
  "name": "FileManipulation",
  "items": [
    {
      "inner_content": null,
      "ai_model_id": null,
      "metadata": {},
      "content_type": "text",
      "text": "# Grouping by category and summing the sales totals to find which category had the most sales\r\nsales_by_category = df.groupby('category')['sales_totals'].sum().reset_index()\r\n\r\n# Identifying the category with the maximum sales\r\nmax_sales_category = sales_by_category.loc[sales_by_category['sales_totals'].idxmax()]\r\n\r\nmax_sales_category",
      "encoding": null
    }
  ],
  "encoding": null,
  "finish_reason": null
}
```

```json
{
  "inner_content": null,
  "ai_model_id": null,
  "metadata": {},
  "content_type": "message",
  "role": "assistant",
  "name": "FileManipulation",
  "items": [
    {
      "inner_content": null,
      "ai_model_id": null,
      "metadata": {},
      "content_type": "text",
      "text": "The category with the most sales is **Home & Kitchen**, with total sales amounting to approximately **6058.62**.",
      "encoding": null
    }
  ],
  "encoding": null,
  "finish_reason": null
}
```
