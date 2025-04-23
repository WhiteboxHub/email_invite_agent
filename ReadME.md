# Email Invite Agent

This project creates an email invite agent that uses an SMTP server to send email invites. It leverages a fine-tuned T5 model to convert text into JSON format, which is then used to send emails. The fine-tuning process is handled using the Modal library to take advantage of free GPU access.

## Project Structure

```
└── 📁src
    └── 📁dataset
        └── fineTune_data.json
        └── finetune_test.json
    └── 📁utils
        └── 📁__pycache__
            └── prompts.cpython-310.pyc
        └── prompts.py
    └── email_connection.py
    └── fine_tune_model_llama2.py
    └── finetune_llm_model.py
    └── llm_model.py
    └── t5_model_finetuing.py
```

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd email-invite-agent
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure SMTP settings:**

   Create a `.env` file in the root directory and add your SMTP credentials:

   ```env
   
   EMAIL_USER=your_smtp_user
   EMAIL_PASS=your_smtp_password
   ```

4. **Fine-tune the T5 model:**

   Ensure you have the Modal CLI installed and configured:

   ```bash
   pip install modal
   modal init
   ```

   Run the fine-tuning script using Modal:

   ```bash
   modal run src/t5_model_finetuing.py
   ```

5. **Run the email invite agent:**

   ```bash
   python src/email_connection.py
   ```

## Fine-tuning with Modal

The fine-tuning process is handled using the Modal library to leverage free GPU access. The `t5_model_finetuing.py` script is designed to run on Modal's infrastructure.

### Steps to Fine-tune the Model

1. **Prepare your dataset:**

   Ensure your dataset is in the `src/dataset` directory with the following files:

   - `fineTune_data.json`: Training data.
   - `finetune_test.json`: Test data.

2. **Run the fine-tuning script:**

   ```bash
   modal run src/t5_model_finetuing.py
   ```

   This command will trigger the fine-tuning process on Modal's infrastructure, utilizing free GPU access.

## Usage

1. **Prepare your invite text:**

   Create a JSON file with the invite text in the `src/dataset` directory.

2. **Run the agent:**

   ```bash
   python src/email_connection.py
   ```

   The agent will convert the text to JSON using the fine-tuned T5 model and send email invites via SMTP.

## Contributing

Feel free to open issues or pull requests to contribute to this project.

## License

This project is licensed under the MIT License.# Email Invite Agent

This project creates an email invite agent that uses an SMTP server to send email invites. It leverages a fine-tuned T5 model to convert text into JSON format, which is then used to send emails. The fine-tuning process is handled using the Modal library to take advantage of free GPU access.

## Project Structure

```
└── 📁src
    └── 📁dataset
        └── fineTune_data.json
        └── finetune_test.json
    └── 📁utils
        └── 📁__pycache__
            └── prompts.cpython-310.pyc
        └── prompts.py
    └── email_connection.py
    └── fine_tune_model_llama2.py
    └── finetune_llm_model.py
    └── llm_model.py
    └── t5_model_finetuing.py
```

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd email-invite-agent
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure SMTP settings:**

   Create a `.env` file in the root directory and add your SMTP credentials:

   ```env
   SMTP_HOST=your_smtp_host
   SMTP_PORT=your_smtp_port
   SMTP_USER=your_smtp_user
   SMTP_PASSWORD=your_smtp_password
   ```

4. **Fine-tune the T5 model:**

   Ensure you have the Modal CLI installed and configured:

   ```bash
   pip install modal
   modal init
   ```

   Run the fine-tuning script using Modal:

   ```bash
   modal run src/t5_model_finetuing.py
   ```

5. **Run the email invite agent:**

   ```bash
   python src/email_connection.py
   ```

## Fine-tuning with Modal

The fine-tuning process is handled using the Modal library to leverage free GPU access. The `t5_model_finetuing.py` script is designed to run on Modal's infrastructure.

### Steps to Fine-tune the Model

1. **Prepare your dataset:**

   Ensure your dataset is in the `src/dataset` directory with the following files:

   - `fineTune_data.json`: Training data.
   - `finetune_test.json`: Test data.

2. **Run the fine-tuning script:**

   ```bash
   modal run src/t5_model_finetuing.py
   ```

   This command will trigger the fine-tuning process on Modal's infrastructure, utilizing free GPU access.

## Usage

1. **Prepare your invite text:**

   Create a JSON file with the invite text in the `src/dataset` directory.

2. **Run the agent:**

   ```bash
   python src/email_connection.py
   ```

   The agent will convert the text to JSON using the fine-tuned T5 model and send email invites via SMTP.
