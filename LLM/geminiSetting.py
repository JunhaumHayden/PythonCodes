#Configurações iniciais
GOOGLE_API_KEY='AIzaSyAOF_fioAmQLzEYKnaIsacResDbxEr4E0A'

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}
#The safety_settings argument lets you configure what the model blocks and allows in both prompts and responses.
safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }