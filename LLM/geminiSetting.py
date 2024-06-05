

GENERATION_CONFIG = {
  "candidate_count": 1,
  "temperature": 0.5,
}
#The safety_settings argument lets you configure what the model blocks and allows in both prompts and responses.
SAFETY_SETTING={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }