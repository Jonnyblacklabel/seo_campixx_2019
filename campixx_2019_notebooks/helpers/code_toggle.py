# =============================================================================
# Hide code toggle
# =============================================================================
from IPython.display import HTML
from IPython.display import display


def main():
  display(HTML("""
  <script>
  code_show=true; 
  function code_toggle() {
    if (code_show){
      $('div.input').hide();
    } else {
      $('div.input').show();
    }
  code_show = !code_show
  } 
  $( document ).ready(code_toggle);
  </script>
  <form action="javascript:code_toggle()">
    <input class="btn btn-secondary btn-sm btn-block" type="submit" value="Click here to toggle on/off the raw code.">
  </form>
  """))
  
if __name__ == '__main__':
  main()
