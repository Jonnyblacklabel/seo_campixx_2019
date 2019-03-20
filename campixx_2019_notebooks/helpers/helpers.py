# =============================================================================
# gsc calc and assign
# =============================================================================
def assign_pos_imp(df):
  """Calculate pos_imp for weighted position
  
  Arguments:
    df -- source DataFrame
  """
  return df.assign(pos_imp=lambda x: x.position * x.impressions)

def assign_position(df):
  """Calculate position and assign new col "position"
  
  Arguments:
    df -- source DataFrame
  """
  return df.assign(position=lambda x: x.pos_imp / x.impressions)


def assign_ctr(df):
  """calculate ctr and assign new col "position"
  
  Arguments:
    df -- source DataFrame
  """
  return df.assign(ctr= lambda x: x.clicks / x.impressions)


# =============================================================================
# plotting
# =============================================================================
sns.set(context='talk',
        rc={'figure.figsize':(15,6),
            'axes.titlepad':18,
            'axes.titlesize':22,
            'figure.constrained_layout.use':True})



# =============================================================================
# gsc segmentation stuff
# =============================================================================
def assign_pattern_column(df, string_col, new_col, pattern, value):
  if new_col not in df.columns:
    df[new_col] = 'undefined'
  df.loc[df[string_col].str.contains(pattern, case=False, regex=True), new_col] = value
  return df


def segment_brand(df, segments):
  """Segment GSC query column for brand pattern and add brand_nonbrand
  column.
  
  Multiple regex patterns in list (or)
  Segments need to be a dict like so:
  {
    "brand_patterns" : ["pattern1", "pattern2"]
  }
  
  Arguments:
    df -- Source DataFrame
    segments -- dict
  """
  pattern = '|'.join(segments['brand_patterns'])
  df = df.assign(brand_nonbrand = 'nonbrand') \
         .pipe(assign_pattern_column,
               string_col = 'query',
               new_col = 'brand_nonbrand',
               pattern = pattern,
               value = 'brand')
  return df


def segment_pages(df, segments):
  """Segment GSC page column and add new columns
  
  Multiple columns can be generated.
  Multiple row values per column.
  Multiple regex patterns in list (or)
  Segments need to be a dict like so:
  {
    "page_patterns" : {
      "col_name" : {
        "row_value" : ["pattern1","pattern2"],
        "startseite" : ["unicef.de/$"]
      }
    }
  }
  
  Arguments:
    df -- Source DataFrame
    segments -- dict
  """
  for new_col, groups in tqdm_notebook(segments['page_patterns'].items(), desc='page segments'):
    df[new_col] = 'unknown'
    for value, patterns in tqdm_notebook(groups.items(), desc='patterns'):
      pattern = '|'.join(patterns)
      df = df.pipe(assign_pattern_column,
                   string_col = 'page',
                   new_col = new_col,
                   pattern = pattern,
                   value = value)
  return df
