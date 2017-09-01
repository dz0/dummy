"""Key examples to csv2df parser.

Workflow as follows (doc/pseudo.rst)

+----------------------------------------------+--------------------------+
| Step                                         | Call                     |
+==============================================+==========================+
| 1. Open csv file as connection               | reader.open_csv()        |
+----------------------------------------------+--------------------------+
| 2. Convert file to list of Rows instances    |                          |
+----------------------------------------------+                          |
| 3. Split list to segments and                |                          |
|    get parsing definition for each segment   | reader.Reader().items()  |
+----------------------------------------------+                          |
| 4. Supply segment and a parsing definition   |                          |
|    for further processing                    |                          |
+----------------------------------------------+--------------------------+
| 5. Create Table instances from rows          |                          |
|                                              | parser.extract_tables()  |
+----------------------------------------------+                          |
| 6. Extract variable name and unit of         |                          |
|    measurement from each table               |                          |
+----------------------------------------------+                          |
| 7. Filter defined tables and check all       |                          |
|    required variables were read              |                          |
+----------------------------------------------+--------------------------+
| 8. Submit tables to Emitter instance         |                          |
+----------------------------------------------+                          |
| 9. Import datapoints from table datarows     | emitter.Emitter()        |
|    by frequency                              |                          |
+----------------------------------------------+                          |
| 10. Create dataframes from datapoints        |                          |
|     by frequency                             |                          |
+----------------------------------------------+--------------------------+
| 11. Validate data in dataframes              | validator.Validator()    |
+----------------------------------------------+--------------------------+
| 12. Save dataframes as csv files             | Vintage().save()         |
+----------------------------------------------+--------------------------+
"""

year, month = 2017, 5
# 3.2 Access to csv file using Vintage class (identical to 3.1)
from csv2df.runner import Vintage


####################  PyCallGraph
from pycallgraph import PyCallGraph
from pycallgraph import GlobbingFilter
from pycallgraph import Config
from pycallgraph import Grouper
from pycallgraph.output import GraphvizOutput

config = Config()

# needed to group by submodules
config.trace_grouper = Grouper(groups=[
        "csv2df.reader.*" ,
        "csv2df.parser.*" ,
        "csv2df.emitter.*" ,
        "csv2df.validator.*" ,  # currently not used
        "csv2df.runner.*" ,

        'csv2df.util_row_splitter.*',
        'csv2df.specification.*',
    ])

config.trace_filter = GlobbingFilter
config.trace_filter = GlobbingFilter(exclude=[
        'csv2df.util_row_splitter.*',
        'csv2df.specification.*',
        "csv2df.reader.*" ,
        
        "config.*" , 


])

graphviz = GraphvizOutput()
graphviz.output_file = 'pcg_example_Vintage.svg'
graphviz.output_type = 'svg'

with PyCallGraph(output=graphviz, config=config):
#################### END PyCallGraph "decoration"
    vint = Vintage(year, month)

