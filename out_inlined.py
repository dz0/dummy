
#@inline 1: csv2df.reader. Reader.__init__ 
def __init__(self, csvfile, spec):
    self.rows = list(to_rows(csvfile))
    #@inline 2: csv2df.reader. to_rows 
    def to_rows(csvfile):
        csv_rows = yield_csv_rows(csvfile)
        csv_rows = filter_csv_rows(csv_rows)
        #@inline 3: csv2df.reader. filter_csv_rows 
        def filter_csv_rows(gen):
            filled = filter(lambda row: row and row[0], gen)
            no_comments = filter(lambda row: not row[0].startswith("___"), filled)
            return no_comments
        #@return: filter_csv_rows => <filter object at 0x7fa48c1dbe...
        return map(Row, csv_rows)
    #@return: to_rows => <map object at 0x7fa499e6e3c8>
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
        for row in csv.reader(csvfile, **fmt):
            yield row
    #@return: yield_csv_rows => []
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => []
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['', 'Год / Year', 'Кварталы /...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['', '', 'I', 'II', 'III', 'IV...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['1. Сводные показатели / Aggr...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 1. Сводные показатели / Aggreg...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
        self.name = row[0]
        self.data = row[1:]
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['1.1. Валовой внутренний прод...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 1.1. Валовой внутренний продук...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['Объем ВВП, млрд.рублей /GDP,...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => Объем ВВП, млрд.рублей /GDP, b...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['20152)', '83233', '18568', '...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 20152)
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['20162)', '86044', '18816', '...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 20162)
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2017', '', '200913)', '', ''...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2017
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => []
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => []
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['Год / Year', 'Кварталы / Qua...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => Год / Year
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['', '', 'I', 'II', 'III', 'IV...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['1.2. Индекс промышленного пр...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 1.2. Индекс промышленного прои...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['Индекс промышленного произво...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => Индекс промышленного производс...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['в % к соответствующему перио...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => в % к соответствующему периоду...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2015', '99,2', '99,9', '98,3...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2015
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2016', '101,3', '101,1', '10...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2016
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2017', '', '100,1', '', '', ...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2017
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['в % к предыдущему периоду / ...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => в % к предыдущему периоду / pe...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2015', '', '82,8', '102,6', ...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2015
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2016', '', '84,4', '103,1', ...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2016
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2017', '', '83,1', '', '', '...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2017
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['период с начала отчетного го...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => период с начала отчетного года...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2015', '', '', '', '', '', '...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2015
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2016', '', '', '', '', '', '...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2016
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['2017', '', '', '', '', '', '...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 2017
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['', 'Янв. Jan.', 'Фев. Feb.',...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => ['1.2.1. Индексы производства ...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09b5d0]_csv2df.reader-74 
    filled = filter(lambda row: row and row[0], gen)
    #@return: <lambda> => 1.2.1. Индексы производства по...
    #@inline 2: csv2df.reader. <lambda>[0x7fa48c09bc00]_csv2df.reader-75 
    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
    #@return: <lambda> => True
    #@inline 2: csv2df.reader. Row.__init__ 
    def __init__(self, row):
    #@return: __init__ => None
    #@inline 2: csv2df.reader. yield_csv_rows 
    def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
    #@return: yield_csv_rows => None
    self.spec = spec
#@return: __init__ => None
#@inline 1: csv2df.reader. Reader.items 
def items(self):
    rowstack = RowStack(self.rows)
    #@inline 2: csv2df.reader. RowStack.__init__ 
    def __init__(self, rows):
        self.rows = list(rows)
    #@return: __init__ => None
    return rowstack.yield_segment_with_defintion(self.spec)
#@return: items => <generator object RowStack.yie...
#@inline 1: csv2df.reader. RowStack.yield_segment_with_defintion 
def yield_segment_with_defintion(self, spec):
    for pdef in spec.get_segment_parsing_definitions():
    #@inline 2: csv2df.specification. Specification.get_segment_parsing_definitions 
    def get_segment_parsing_definitions(self):
        return self.segment_definitions
    #@return: get_segment_parsing_definitions => []
    yield self.remaining_rows(), spec.get_main_parsing_definition()
    #@inline 2: csv2df.reader. RowStack.remaining_rows 
    def remaining_rows(self):
        remaining = self.rows
        self.rows = []
        return remaining
    #@return: remaining_rows => [Row(['1. Сводные показатели /...
    #@inline 2: csv2df.specification. Specification.get_main_parsing_definition 
    def get_main_parsing_definition(self):
        return self.main
    #@return: get_main_parsing_definition => <csv2df.specification.Definiti...
#@return: yield_segment_with_defintion => ([Row(['1. Сводные показатели ...
#@inline 1: csv2df.parser. extract_tables 
def extract_tables(csv_segment, pdef):
    tables = split_to_tables(csv_segment)
    tables = parse_tables(tables, pdef)
    #@inline 2: csv2df.parser. parse_tables 
    def parse_tables(tables, pdef):
        tables = [t.set_label(pdef.varnames_dict, pdef.units_dict) for t in tables]
        #@inline 3: csv2df.parser. split_to_tables 
        def split_to_tables(rows):
            datarows = []
            headers = []
            state = State.INIT
            for row in rows:
                if row.is_datarow():
                #@inline 4: csv2df.reader. Row.is_datarow 
                def is_datarow(self):
                    return is_year(self.name)
                    #@inline 5: csv2df.reader. is_year 
                    def is_year(string: str) -> bool:
                        return get_year(string) is not False
                        #@inline 6: csv2df.reader. get_year 
                        def get_year(string: str, rx=YEAR_CATCHER):
                            match = re.match(rx, string)
                            if match:
                            return False
                        #@return: get_year => False
                    #@return: is_year => False
                #@return: is_datarow => False
                    if state == State.DATA:  # table ended
                    headers.append(row)
                    state = State.UNKNOWN
                    #@inline 4: csv2df.reader. Row.is_datarow 
                    def is_datarow(self):
                    #@inline 5: csv2df.reader. is_year 
                    def is_year(string: str) -> bool:
                    #@inline 6: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                    #@return: get_year => False
                    #@return: is_year => False
                    #@return: is_datarow => False
                    #@inline 4: csv2df.reader. Row.is_datarow 
                    def is_datarow(self):
                    #@inline 5: csv2df.reader. is_year 
                    def is_year(string: str) -> bool:
                    #@inline 6: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                    #@return: get_year => False
                    #@return: is_year => False
                    #@return: is_datarow => False
                    #@inline 4: csv2df.reader. Row.is_datarow 
                    def is_datarow(self):
                    #@inline 5: csv2df.reader. is_year 
                    def is_year(string: str) -> bool:
                    #@inline 6: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                            year = int(match.group(1))
                            if year >= 1991 and year <= 2050:
                                return year
                    #@return: get_year => 2015
                    #@return: is_year => True
                    #@return: is_datarow => True
                    datarows.append(row)
                    state = State.DATA
                    #@inline 4: csv2df.reader. Row.is_datarow 
                    def is_datarow(self):
                    #@inline 5: csv2df.reader. is_year 
                    def is_year(string: str) -> bool:
                    #@inline 6: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                    #@return: get_year => 2016
                    #@return: is_year => True
                    #@return: is_datarow => True
                    #@inline 4: csv2df.reader. Row.is_datarow 
                    def is_datarow(self):
                    #@inline 5: csv2df.reader. is_year 
                    def is_year(string: str) -> bool:
                    #@inline 6: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                    #@return: get_year => 2017
                    #@return: is_year => True
                    #@return: is_datarow => True
                    #@inline 4: csv2df.reader. Row.is_datarow 
                    def is_datarow(self):
                    #@inline 5: csv2df.reader. is_year 
                    def is_year(string: str) -> bool:
                    #@inline 6: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                    #@return: get_year => False
                    #@return: is_year => False
                    #@return: is_datarow => False
                        yield Table(headers, datarows)
                        #@inline 4: csv2df.parser. Table.__init__ 
                        def __init__(self, headers, datarows):
                            self.varname = None
                            self.unit = None
                            self.headers = headers
                            self.lines = odict((row.name, self.UNKNOWN) for row in headers)
                            self.datarows = datarows
                            self.coln = max(len(row) for row in self.datarows)
                            #@inline 5: csv2df.reader. Row.__len__ 
                            def __len__(self):
                                return len(self.data)
                            #@return: __len__ => 5
                            #@inline 5: csv2df.reader. Row.__len__ 
                            def __len__(self):
                            #@return: __len__ => 5
                            #@inline 5: csv2df.reader. Row.__len__ 
                            def __len__(self):
                            #@return: __len__ => 5
                            self.splitter_func = None
                        #@return: __init__ => None
        #@return: split_to_tables => Table None (5 columns)
- <1. С...
        #@inline 3: csv2df.specification. Definition.varnames_dict 
        @property
            return self.instr.varname_mapper
        #@return: varnames_dict => OrderedDict([('Объем ВВП', 'GD...
        #@inline 3: csv2df.specification. Definition.units_dict 
        @property
            return self.units
        #@return: units_dict => {'млрд.рублей': 'bln_rub', 'пе...
        #@inline 3: csv2df.parser. Table.set_label 
        def set_label(self, varnames_dict, units_dict):
            for row in self.headers:
                varname = row.get_varname(varnames_dict)
                #@inline 4: csv2df.reader. Row.get_varname 
                def get_varname(self, varnames_mapper_dict):
                    varnames = []
                    for k in varnames_mapper_dict.keys():
                        if self.matches(k):
                        #@inline 5: csv2df.reader. Row.matches 
                        def matches(self, pat):
                            rx = r"\b{}".format(pat)
                            return bool(re.search(rx, self.name))
                        #@return: matches => False
                        #@inline 5: csv2df.reader. Row.matches 
                        def matches(self, pat):
                        #@return: matches => False
                    if len(varnames) > 1:
                    elif len(varnames) == 1:
                        return False
                #@return: get_varname => False
                if varname:
                unit = row.get_unit(units_dict)
                #@inline 4: csv2df.reader. Row.get_unit 
                def get_unit(self, units_mapper_dict):
                    for k in units_mapper_dict.keys():
                        if k in self.name:
                    return False
                #@return: get_unit => False
                if unit:
                #@inline 4: csv2df.reader. Row.get_varname 
                def get_varname(self, varnames_mapper_dict):
                #@inline 5: csv2df.reader. Row.matches 
                def matches(self, pat):
                #@return: matches => False
                #@inline 5: csv2df.reader. Row.matches 
                def matches(self, pat):
                #@return: matches => False
                #@return: get_varname => False
                #@inline 4: csv2df.reader. Row.get_unit 
                def get_unit(self, units_mapper_dict):
                #@return: get_unit => False
                #@inline 4: csv2df.reader. Row.get_varname 
                def get_varname(self, varnames_mapper_dict):
                #@inline 5: csv2df.reader. Row.matches 
                def matches(self, pat):
                #@return: matches => True
                            varnames.append(varnames_mapper_dict[k])
                            #@inline 5: csv2df.reader. Row.matches 
                            def matches(self, pat):
                            #@return: matches => False
                        return varnames[0]
                #@return: get_varname => GDP
                    self.varname = varname
                    self.lines[row.name] = self.KNOWN
                    #@inline 4: csv2df.reader. Row.get_unit 
                    def get_unit(self, units_mapper_dict):
                                return units_mapper_dict[k]
                    #@return: get_unit => bln_rub
                    self.unit = unit
                    self.lines[row.name] = self.KNOWN
            return self
        #@return: set_label => Table GDP_bln_rub (5 columns)
...
        #@inline 3: csv2df.parser. split_to_tables 
        def split_to_tables(rows):
                        headers = []
                        datarows = []
                        #@inline 4: csv2df.reader. Row.is_datarow 
                        def is_datarow(self):
                        #@inline 5: csv2df.reader. is_year 
                        def is_year(string: str) -> bool:
                        #@inline 6: csv2df.reader. get_year 
                        def get_year(string: str, rx=YEAR_CATCHER):
                        #@return: get_year => False
                        #@return: is_year => False
                        #@return: is_datarow => False
                        #@inline 4: csv2df.reader. Row.is_datarow 
                        def is_datarow(self):
                        #@inline 5: csv2df.reader. is_year 
                        def is_year(string: str) -> bool:
                        #@inline 6: csv2df.reader. get_year 
                        def get_year(string: str, rx=YEAR_CATCHER):
                        #@return: get_year => False
                        #@return: is_year => False
                        #@return: is_datarow => False
                        #@inline 4: csv2df.reader. Row.is_datarow 
                        def is_datarow(self):
                        #@inline 5: csv2df.reader. is_year 
                        def is_year(string: str) -> bool:
                        #@inline 6: csv2df.reader. get_year 
                        def get_year(string: str, rx=YEAR_CATCHER):
                        #@return: get_year => False
                        #@return: is_year => False
                        #@return: is_datarow => False
                        #@inline 4: csv2df.reader. Row.is_datarow 
                        def is_datarow(self):
                        #@inline 5: csv2df.reader. is_year 
                        def is_year(string: str) -> bool:
                        #@inline 6: csv2df.reader. get_year 
                        def get_year(string: str, rx=YEAR_CATCHER):
                        #@return: get_year => 2015
                        #@return: is_year => True
                        #@return: is_datarow => True
                        #@inline 4: csv2df.reader. Row.is_datarow 
                        def is_datarow(self):
                        #@inline 5: csv2df.reader. is_year 
                        def is_year(string: str) -> bool:
                        #@inline 6: csv2df.reader. get_year 
                        def get_year(string: str, rx=YEAR_CATCHER):
                        #@return: get_year => 2016
                        #@return: is_year => True
                        #@return: is_datarow => True
                        #@inline 4: csv2df.reader. Row.is_datarow 
                        def is_datarow(self):
                        #@inline 5: csv2df.reader. is_year 
                        def is_year(string: str) -> bool:
                        #@inline 6: csv2df.reader. get_year 
                        def get_year(string: str, rx=YEAR_CATCHER):
                        #@return: get_year => 2017
                        #@return: is_year => True
                        #@return: is_datarow => True
                        #@inline 4: csv2df.reader. Row.is_datarow 
                        def is_datarow(self):
                        #@inline 5: csv2df.reader. is_year 
                        def is_year(string: str) -> bool:
                        #@inline 6: csv2df.reader. get_year 
                        def get_year(string: str, rx=YEAR_CATCHER):
                        #@return: get_year => False
                        #@return: is_year => False
                        #@return: is_datarow => False
                        #@inline 4: csv2df.parser. Table.__init__ 
                        def __init__(self, headers, datarows):
                        #@inline 5: csv2df.reader. Row.__len__ 
                        def __len__(self):
                        #@return: __len__ => 17
                        #@inline 5: csv2df.reader. Row.__len__ 
                        def __len__(self):
                        #@return: __len__ => 17
                        #@inline 5: csv2df.reader. Row.__len__ 
                        def __len__(self):
                        #@return: __len__ => 17
                        #@return: __init__ => None
        #@return: split_to_tables => Table None (17 columns)
- <Год...
        #@inline 3: csv2df.specification. Definition.varnames_dict 
        @property
        #@return: varnames_dict => OrderedDict([('Объем ВВП', 'GD...
        #@inline 3: csv2df.specification. Definition.units_dict 
        @property
        #@return: units_dict => {'млрд.рублей': 'bln_rub', 'пе...
        #@inline 3: csv2df.parser. Table.set_label 
        def set_label(self, varnames_dict, units_dict):
        #@inline 4: csv2df.reader. Row.get_varname 
        def get_varname(self, varnames_mapper_dict):
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@return: get_varname => False
        #@inline 4: csv2df.reader. Row.get_unit 
        def get_unit(self, units_mapper_dict):
        #@return: get_unit => False
        #@inline 4: csv2df.reader. Row.get_varname 
        def get_varname(self, varnames_mapper_dict):
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => True
        #@return: get_varname => INDPRO
        #@inline 4: csv2df.reader. Row.get_unit 
        def get_unit(self, units_mapper_dict):
        #@return: get_unit => False
        #@inline 4: csv2df.reader. Row.get_varname 
        def get_varname(self, varnames_mapper_dict):
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => True
        #@return: get_varname => INDPRO
        #@inline 4: csv2df.reader. Row.get_unit 
        def get_unit(self, units_mapper_dict):
        #@return: get_unit => False
        #@inline 4: csv2df.reader. Row.get_varname 
        def get_varname(self, varnames_mapper_dict):
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@return: get_varname => False
        #@inline 4: csv2df.reader. Row.get_unit 
        def get_unit(self, units_mapper_dict):
        #@return: get_unit => yoy
        #@return: set_label => Table INDPRO_yoy (17 columns)
...
        #@inline 3: csv2df.parser. split_to_tables 
        def split_to_tables(rows):
        #@inline 4: csv2df.reader. Row.is_datarow 
        def is_datarow(self):
        #@inline 5: csv2df.reader. is_year 
        def is_year(string: str) -> bool:
        #@inline 6: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2015
        #@return: is_year => True
        #@return: is_datarow => True
        #@inline 4: csv2df.reader. Row.is_datarow 
        def is_datarow(self):
        #@inline 5: csv2df.reader. is_year 
        def is_year(string: str) -> bool:
        #@inline 6: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2016
        #@return: is_year => True
        #@return: is_datarow => True
        #@inline 4: csv2df.reader. Row.is_datarow 
        def is_datarow(self):
        #@inline 5: csv2df.reader. is_year 
        def is_year(string: str) -> bool:
        #@inline 6: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2017
        #@return: is_year => True
        #@return: is_datarow => True
        #@inline 4: csv2df.reader. Row.is_datarow 
        def is_datarow(self):
        #@inline 5: csv2df.reader. is_year 
        def is_year(string: str) -> bool:
        #@inline 6: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => False
        #@return: is_year => False
        #@return: is_datarow => False
        #@inline 4: csv2df.parser. Table.__init__ 
        def __init__(self, headers, datarows):
        #@inline 5: csv2df.reader. Row.__len__ 
        def __len__(self):
        #@return: __len__ => 17
        #@inline 5: csv2df.reader. Row.__len__ 
        def __len__(self):
        #@return: __len__ => 17
        #@inline 5: csv2df.reader. Row.__len__ 
        def __len__(self):
        #@return: __len__ => 17
        #@return: __init__ => None
        #@return: split_to_tables => Table None (17 columns)
- <в %...
        #@inline 3: csv2df.specification. Definition.varnames_dict 
        @property
        #@return: varnames_dict => OrderedDict([('Объем ВВП', 'GD...
        #@inline 3: csv2df.specification. Definition.units_dict 
        @property
        #@return: units_dict => {'млрд.рублей': 'bln_rub', 'пе...
        #@inline 3: csv2df.parser. Table.set_label 
        def set_label(self, varnames_dict, units_dict):
        #@inline 4: csv2df.reader. Row.get_varname 
        def get_varname(self, varnames_mapper_dict):
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@return: get_varname => False
        #@inline 4: csv2df.reader. Row.get_unit 
        def get_unit(self, units_mapper_dict):
        #@return: get_unit => rog
        #@return: set_label => Table None (17 columns)
+ <в %...
        #@inline 3: csv2df.parser. split_to_tables 
        def split_to_tables(rows):
        #@inline 4: csv2df.reader. Row.is_datarow 
        def is_datarow(self):
        #@inline 5: csv2df.reader. is_year 
        def is_year(string: str) -> bool:
        #@inline 6: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2015
        #@return: is_year => True
        #@return: is_datarow => True
        #@inline 4: csv2df.reader. Row.is_datarow 
        def is_datarow(self):
        #@inline 5: csv2df.reader. is_year 
        def is_year(string: str) -> bool:
        #@inline 6: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2016
        #@return: is_year => True
        #@return: is_datarow => True
        #@inline 4: csv2df.reader. Row.is_datarow 
        def is_datarow(self):
        #@inline 5: csv2df.reader. is_year 
        def is_year(string: str) -> bool:
        #@inline 6: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2017
        #@return: is_year => True
        #@return: is_datarow => True
        #@inline 4: csv2df.reader. Row.is_datarow 
        def is_datarow(self):
        #@inline 5: csv2df.reader. is_year 
        def is_year(string: str) -> bool:
        #@inline 6: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => False
        #@return: is_year => False
        #@return: is_datarow => False
        #@inline 4: csv2df.parser. Table.__init__ 
        def __init__(self, headers, datarows):
        #@inline 5: csv2df.reader. Row.__len__ 
        def __len__(self):
        #@return: __len__ => 17
        #@inline 5: csv2df.reader. Row.__len__ 
        def __len__(self):
        #@return: __len__ => 17
        #@inline 5: csv2df.reader. Row.__len__ 
        def __len__(self):
        #@return: __len__ => 17
        #@return: __init__ => None
        #@return: split_to_tables => Table None (17 columns)
- <пер...
        #@inline 3: csv2df.specification. Definition.varnames_dict 
        @property
        #@return: varnames_dict => OrderedDict([('Объем ВВП', 'GD...
        #@inline 3: csv2df.specification. Definition.units_dict 
        @property
        #@return: units_dict => {'млрд.рублей': 'bln_rub', 'пе...
        #@inline 3: csv2df.parser. Table.set_label 
        def set_label(self, varnames_dict, units_dict):
        #@inline 4: csv2df.reader. Row.get_varname 
        def get_varname(self, varnames_mapper_dict):
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@inline 5: csv2df.reader. Row.matches 
        def matches(self, pat):
        #@return: matches => False
        #@return: get_varname => False
        #@inline 4: csv2df.reader. Row.get_unit 
        def get_unit(self, units_mapper_dict):
        #@return: get_unit => ytd
        #@return: set_label => Table None (17 columns)
+ <пер...
        #@inline 3: csv2df.parser. split_to_tables 
        def split_to_tables(rows):
            if len(headers) > 0 and len(datarows) > 0:
        #@return: split_to_tables => None
        tables = [t.set_splitter(pdef.funcname) for t in tables]
        #@inline 3: csv2df.specification. Definition.funcname 
        @property
            return self.reader
        #@return: funcname => False
        #@inline 3: csv2df.parser. Table.set_splitter 
        def set_splitter(self, funcname):
            self.splitter_func = splitter.get_splitter(funcname or self.coln)
            #@inline 4: csv2df.util_row_splitter. get_splitter 
            def get_splitter(arg):
                try:
                    return FUNC_MAPPER[arg]
            #@return: get_splitter => <function split_row_by_year_an...
            return self
        #@return: set_splitter => Table GDP_bln_rub (5 columns)
...
        #@inline 3: csv2df.specification. Definition.funcname 
        @property
        #@return: funcname => False
        #@inline 3: csv2df.parser. Table.set_splitter 
        def set_splitter(self, funcname):
        #@inline 4: csv2df.util_row_splitter. get_splitter 
        def get_splitter(arg):
        #@return: get_splitter => <function split_row_by_periods...
        #@return: set_splitter => Table INDPRO_yoy (17 columns)
...
        #@inline 3: csv2df.specification. Definition.funcname 
        @property
        #@return: funcname => False
        #@inline 3: csv2df.parser. Table.set_splitter 
        def set_splitter(self, funcname):
        #@inline 4: csv2df.util_row_splitter. get_splitter 
        def get_splitter(arg):
        #@return: get_splitter => <function split_row_by_periods...
        #@return: set_splitter => Table None (17 columns)
+ <в %...
        #@inline 3: csv2df.specification. Definition.funcname 
        @property
        #@return: funcname => False
        #@inline 3: csv2df.parser. Table.set_splitter 
        def set_splitter(self, funcname):
        #@inline 4: csv2df.util_row_splitter. get_splitter 
        def get_splitter(arg):
        #@return: get_splitter => <function split_row_by_periods...
        #@return: set_splitter => Table None (17 columns)
+ <пер...
        def fix_multitable_units(tables):
        fix_multitable_units(tables)
        #@inline 3: csv2df.parser. fix_multitable_units 
        def fix_multitable_units(tables):
            for prev_table, table in zip(tables, tables[1:]):
                if table.varname is None and not table.has_unknown_lines():
                #@inline 4: csv2df.parser. Table.has_unknown_lines 
                def has_unknown_lines(self):
                    return self.UNKNOWN in self.lines.values()
                #@return: has_unknown_lines => False
                    table.varname = prev_table.varname
                    #@inline 4: csv2df.parser. Table.has_unknown_lines 
                    def has_unknown_lines(self):
                    #@return: has_unknown_lines => False
        #@return: fix_multitable_units => None
        return tables
    #@return: parse_tables => [Table(headers=[Row(['1. Сводн...
    verify_tables(tables, pdef)
    #@inline 2: csv2df.parser. verify_tables 
    def verify_tables(tables, pdef):
        _labels_in_tables = [t.label for t in tables]
        #@inline 3: csv2df.parser. Table.label 
        @property
            vn = self.varname
            u = self.unit
            if vn and u:
                return make_label(vn, u)
                #@inline 4: csv2df.util_label. make_label 
                def make_label(vn, unit, sep=SEP):
                    return vn + sep + unit
                #@return: make_label => GDP_bln_rub
        #@return: label => GDP_bln_rub
        #@inline 3: csv2df.parser. Table.label 
        @property
        #@inline 4: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_yoy
        #@return: label => INDPRO_yoy
        #@inline 3: csv2df.parser. Table.label 
        @property
        #@inline 4: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_rog
        #@return: label => INDPRO_rog
        #@inline 3: csv2df.parser. Table.label 
        @property
        #@inline 4: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_ytd
        #@return: label => INDPRO_ytd
        _labels_missed = [x for x in pdef.required if x not in _labels_in_tables]
        #@inline 3: csv2df.specification. Definition.required 
        @property
            return self.instr.required_labels
        #@return: required => ['GDP_bln_rub', 'INDPRO_yoy', ...
        if _labels_missed:
    #@return: verify_tables => None
    return [t for t in tables if t.label in pdef.required]
    #@inline 2: csv2df.parser. Table.label 
    @property
    #@inline 3: csv2df.util_label. make_label 
    def make_label(vn, unit, sep=SEP):
    #@return: make_label => GDP_bln_rub
    #@return: label => GDP_bln_rub
    #@inline 2: csv2df.specification. Definition.required 
    @property
    #@return: required => ['GDP_bln_rub', 'INDPRO_yoy', ...
    #@inline 2: csv2df.parser. Table.label 
    @property
    #@inline 3: csv2df.util_label. make_label 
    def make_label(vn, unit, sep=SEP):
    #@return: make_label => INDPRO_yoy
    #@return: label => INDPRO_yoy
    #@inline 2: csv2df.specification. Definition.required 
    @property
    #@return: required => ['GDP_bln_rub', 'INDPRO_yoy', ...
    #@inline 2: csv2df.parser. Table.label 
    @property
    #@inline 3: csv2df.util_label. make_label 
    def make_label(vn, unit, sep=SEP):
    #@return: make_label => INDPRO_rog
    #@return: label => INDPRO_rog
    #@inline 2: csv2df.specification. Definition.required 
    @property
    #@return: required => ['GDP_bln_rub', 'INDPRO_yoy', ...
    #@inline 2: csv2df.parser. Table.label 
    @property
    #@inline 3: csv2df.util_label. make_label 
    def make_label(vn, unit, sep=SEP):
    #@return: make_label => INDPRO_ytd
    #@return: label => INDPRO_ytd
    #@inline 2: csv2df.specification. Definition.required 
    @property
    #@return: required => ['GDP_bln_rub', 'INDPRO_yoy', ...
#@return: extract_tables => [Table(headers=[Row(['1. Сводн...
#@inline 1: csv2df.reader. RowStack.yield_segment_with_defintion 
def yield_segment_with_defintion(self, spec):
#@return: yield_segment_with_defintion => None
#@inline 1: csv2df.emitter. Emitter.__init__ 
def __init__(self, tables):
    self.a = []
    self.q = []
    self.m = []
    for t in tables:
        self._assert_defined(t)
        #@inline 2: csv2df.emitter. _assert_defined 
        @staticmethod
            if not table.is_defined():
            #@inline 3: csv2df.parser. Table.is_defined 
            def is_defined(self):
                return bool(self.label and self.splitter_func)
                #@inline 4: csv2df.parser. Table.label 
                @property
                #@inline 5: csv2df.util_label. make_label 
                def make_label(vn, unit, sep=SEP):
                #@return: make_label => GDP_bln_rub
                #@return: label => GDP_bln_rub
            #@return: is_defined => True
        #@return: _assert_defined => None
        self._import(t)
        #@inline 2: csv2df.emitter. Emitter._import 
        def _import(self, table):
            for row in table.datarows:
                factory = DatapointMaker(row.get_year(), table.label)
                #@inline 3: csv2df.reader. Row.get_year 
                def get_year(self):
                    return get_year(self.name)
                    #@inline 4: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                    #@return: get_year => 2015
                #@return: get_year => 2015
                #@inline 3: csv2df.parser. Table.label 
                @property
                #@inline 4: csv2df.util_label. make_label 
                def make_label(vn, unit, sep=SEP):
                #@return: make_label => GDP_bln_rub
                #@return: label => GDP_bln_rub
                #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
                def __init__(self, year, label):
                    self.year = year
                    self.label = label
                    self.freq = False
                    self.value = False
                    self.period = False
                #@return: __init__ => None
                a_value, q_values, m_values = table.splitter_func(row.data)
                #@inline 3: csv2df.util_row_splitter. split_row_by_year_and_qtr 
                def split_row_by_year_and_qtr(row):
                    return row[0], row[1:1 + 4], None
                #@return: split_row_by_year_and_qtr => ('83233', ['18568', '19858', '...
                if a_value:
                    self.a.append(factory.make('a', a_value))
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                        self.freq = freq
                        self.set_value(x)
                        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                        def set_value(self, x):
                            if x:
                                self.value = to_float(x)
                                #@inline 5: csv2df.emitter. to_float 
                                def to_float(text: str, i=0):
                                    i += 1
                                    if i > 5:
                                    if not text:
                                    text = text.replace(",", ".")
                                    try:
                                        return float(text)
                                #@return: to_float => 83233.0
                        #@return: set_value => None
                        self.period = period
                        return self.as_dict()
                        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                        def as_dict(self):
                            basedict = dict(year=int(self.year),
                                            label=self.label,
                                            freq=self.freq,
                                            value=self.value,
                                            time_index=self.get_date())
                            #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                            def get_date(self):
                                if self.freq == 'a':
                                    return pd.Timestamp(str(self.year)) + pd.offsets.YearEnd()
                            #@return: get_date => 2015-12-31 00:00:00
                            if self.freq == 'q':
                            elif self.freq == 'm':
                            return basedict
                        #@return: as_dict => {'year': 2015, 'label': 'GDP_b...
                    #@return: make => {'year': 2015, 'label': 'GDP_b...
                if q_values:
                    qs = [factory.make('q', val, t + 1)
                          for t, val in enumerate(q_values) if val]
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 18568.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                        year = int(self.year)
                        if self.freq == 'q':
                            month = int(self.period) * 3
                            base = pd.Timestamp(year, month, 1)
                            return base + pd.offsets.QuarterEnd()
                    #@return: get_date => 2015-03-31 00:00:00
                            basedict.update(dict(qtr=self.period))
                    #@return: as_dict => {'year': 2015, 'label': 'GDP_b...
                    #@return: make => {'year': 2015, 'label': 'GDP_b...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 19858.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-06-30 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'GDP_b...
                    #@return: make => {'year': 2015, 'label': 'GDP_b...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 21967.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-09-30 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'GDP_b...
                    #@return: make => {'year': 2015, 'label': 'GDP_b...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 22840.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-12-31 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'GDP_b...
                    #@return: make => {'year': 2015, 'label': 'GDP_b...
                    self.q.extend(qs)
                if m_values:
                #@inline 3: csv2df.reader. Row.get_year 
                def get_year(self):
                #@inline 4: csv2df.reader. get_year 
                def get_year(string: str, rx=YEAR_CATCHER):
                #@return: get_year => 2016
                #@return: get_year => 2016
                #@inline 3: csv2df.parser. Table.label 
                @property
                #@inline 4: csv2df.util_label. make_label 
                def make_label(vn, unit, sep=SEP):
                #@return: make_label => GDP_bln_rub
                #@return: label => GDP_bln_rub
                #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
                def __init__(self, year, label):
                #@return: __init__ => None
                #@inline 3: csv2df.util_row_splitter. split_row_by_year_and_qtr 
                def split_row_by_year_and_qtr(row):
                #@return: split_row_by_year_and_qtr => ('86044', ['18816', '20430', '...
                #@inline 3: csv2df.emitter. DatapointMaker.make 
                def make(self, freq: str, x: float, period=False):
                #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                def set_value(self, x):
                #@inline 5: csv2df.emitter. to_float 
                def to_float(text: str, i=0):
                #@return: to_float => 86044.0
                #@return: set_value => None
                #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                def as_dict(self):
                #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                def get_date(self):
                #@return: get_date => 2016-12-31 00:00:00
                #@return: as_dict => {'year': 2016, 'label': 'GDP_b...
                #@return: make => {'year': 2016, 'label': 'GDP_b...
                #@inline 3: csv2df.emitter. DatapointMaker.make 
                def make(self, freq: str, x: float, period=False):
                #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                def set_value(self, x):
                #@inline 5: csv2df.emitter. to_float 
                def to_float(text: str, i=0):
                #@return: to_float => 18816.0
                #@return: set_value => None
                #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                def as_dict(self):
                #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                def get_date(self):
                #@return: get_date => 2016-03-31 00:00:00
                #@return: as_dict => {'year': 2016, 'label': 'GDP_b...
                #@return: make => {'year': 2016, 'label': 'GDP_b...
                #@inline 3: csv2df.emitter. DatapointMaker.make 
                def make(self, freq: str, x: float, period=False):
                #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                def set_value(self, x):
                #@inline 5: csv2df.emitter. to_float 
                def to_float(text: str, i=0):
                #@return: to_float => 20430.0
                #@return: set_value => None
                #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                def as_dict(self):
                #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                def get_date(self):
                #@return: get_date => 2016-06-30 00:00:00
                #@return: as_dict => {'year': 2016, 'label': 'GDP_b...
                #@return: make => {'year': 2016, 'label': 'GDP_b...
                #@inline 3: csv2df.emitter. DatapointMaker.make 
                def make(self, freq: str, x: float, period=False):
                #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                def set_value(self, x):
                #@inline 5: csv2df.emitter. to_float 
                def to_float(text: str, i=0):
                #@return: to_float => 22721.0
                #@return: set_value => None
                #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                def as_dict(self):
                #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                def get_date(self):
                #@return: get_date => 2016-09-30 00:00:00
                #@return: as_dict => {'year': 2016, 'label': 'GDP_b...
                #@return: make => {'year': 2016, 'label': 'GDP_b...
                #@inline 3: csv2df.emitter. DatapointMaker.make 
                def make(self, freq: str, x: float, period=False):
                #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                def set_value(self, x):
                #@inline 5: csv2df.emitter. to_float 
                def to_float(text: str, i=0):
                #@return: to_float => 24077.0
                #@return: set_value => None
                #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                def as_dict(self):
                #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                def get_date(self):
                #@return: get_date => 2016-12-31 00:00:00
                #@return: as_dict => {'year': 2016, 'label': 'GDP_b...
                #@return: make => {'year': 2016, 'label': 'GDP_b...
                #@inline 3: csv2df.reader. Row.get_year 
                def get_year(self):
                #@inline 4: csv2df.reader. get_year 
                def get_year(string: str, rx=YEAR_CATCHER):
                #@return: get_year => 2017
                #@return: get_year => 2017
                #@inline 3: csv2df.parser. Table.label 
                @property
                #@inline 4: csv2df.util_label. make_label 
                def make_label(vn, unit, sep=SEP):
                #@return: make_label => GDP_bln_rub
                #@return: label => GDP_bln_rub
                #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
                def __init__(self, year, label):
                #@return: __init__ => None
                #@inline 3: csv2df.util_row_splitter. split_row_by_year_and_qtr 
                def split_row_by_year_and_qtr(row):
                #@return: split_row_by_year_and_qtr => ('', ['200913)', '', '', ''], ...
                #@inline 3: csv2df.emitter. DatapointMaker.make 
                def make(self, freq: str, x: float, period=False):
                #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                def set_value(self, x):
                #@inline 5: csv2df.emitter. to_float 
                def to_float(text: str, i=0):
                    except ValueError:
                        if " " in text.strip():  # get first value '542,0 5881)'
                        if ")" in text:  # catch '542,01)'
                            match_result = COMMENT_CATCHER.match(text)
                            if match_result:
                                text = match_result.group(0)
                                return to_float(text, i)
                                #@inline 6: csv2df.emitter. to_float 
                                def to_float(text: str, i=0):
                                #@return: to_float => 20091.0
                #@return: to_float => 20091.0
                #@return: set_value => None
                #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                def as_dict(self):
                #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                def get_date(self):
                #@return: get_date => 2017-03-31 00:00:00
                #@return: as_dict => {'year': 2017, 'label': 'GDP_b...
                #@return: make => {'year': 2017, 'label': 'GDP_b...
        #@return: _import => None
        #@inline 2: csv2df.emitter. _assert_defined 
        @staticmethod
        #@inline 3: csv2df.parser. Table.is_defined 
        def is_defined(self):
        #@inline 4: csv2df.parser. Table.label 
        @property
        #@inline 5: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_yoy
        #@return: label => INDPRO_yoy
        #@return: is_defined => True
        #@return: _assert_defined => None
        #@inline 2: csv2df.emitter. Emitter._import 
        def _import(self, table):
        #@inline 3: csv2df.reader. Row.get_year 
        def get_year(self):
        #@inline 4: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2015
        #@return: get_year => 2015
        #@inline 3: csv2df.parser. Table.label 
        @property
        #@inline 4: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_yoy
        #@return: label => INDPRO_yoy
        #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
        def __init__(self, year, label):
        #@return: __init__ => None
        #@inline 3: csv2df.util_row_splitter. split_row_by_periods 
        def split_row_by_periods(row):
            return row[0], row[1:1 + 4], row[1 + 4:1 + 4 + 12]
        #@return: split_row_by_periods => ('99,2', ['99,9', '98,3', '99,...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 99.2
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-12-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 99.9
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-03-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 98.3
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-06-30 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 99.5
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-09-30 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 99.1
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-12-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
                    ms = [factory.make('m', val, t + 1)
                          for t, val in enumerate(m_values) if val]
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 100.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                        elif self.freq == 'm':
                            month = int(self.period)
                            base = pd.Timestamp(year, month, 1)
                            return base + pd.offsets.MonthEnd()
                    #@return: get_date => 2015-01-31 00:00:00
                            basedict.update(dict(month=self.period))
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 98.2
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-02-28 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.2
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-03-31 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 98.2
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-04-30 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 97.6
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-05-31 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 99.1
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-06-30 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 98.5
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-07-31 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 100.2
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-08-31 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 99.7
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-09-30 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 98.4
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-10-31 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-11-30 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 98.1
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2015-12-31 00:00:00
                    #@return: as_dict => {'year': 2015, 'label': 'INDPR...
                    #@return: make => {'year': 2015, 'label': 'INDPR...
                    self.m.extend(ms)
                    #@inline 3: csv2df.reader. Row.get_year 
                    def get_year(self):
                    #@inline 4: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                    #@return: get_year => 2016
                    #@return: get_year => 2016
                    #@inline 3: csv2df.parser. Table.label 
                    @property
                    #@inline 4: csv2df.util_label. make_label 
                    def make_label(vn, unit, sep=SEP):
                    #@return: make_label => INDPRO_yoy
                    #@return: label => INDPRO_yoy
                    #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
                    def __init__(self, year, label):
                    #@return: __init__ => None
                    #@inline 3: csv2df.util_row_splitter. split_row_by_periods 
                    def split_row_by_periods(row):
                    #@return: split_row_by_periods => ('101,3', ['101,1', '101,5', '...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.3
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-12-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.1
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-03-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.5
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-06-30 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-09-30 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.7
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-12-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 99.2
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-01-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 103.8
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-02-29 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 100.3
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-03-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-04-30 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.5
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-05-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 102.0
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-06-30 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.4
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-07-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.5
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-08-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 100.1
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-09-30 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 101.6
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-10-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 103.4
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-11-30 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 100.2
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2016-12-31 00:00:00
                    #@return: as_dict => {'year': 2016, 'label': 'INDPR...
                    #@return: make => {'year': 2016, 'label': 'INDPR...
                    #@inline 3: csv2df.reader. Row.get_year 
                    def get_year(self):
                    #@inline 4: csv2df.reader. get_year 
                    def get_year(string: str, rx=YEAR_CATCHER):
                    #@return: get_year => 2017
                    #@return: get_year => 2017
                    #@inline 3: csv2df.parser. Table.label 
                    @property
                    #@inline 4: csv2df.util_label. make_label 
                    def make_label(vn, unit, sep=SEP):
                    #@return: make_label => INDPRO_yoy
                    #@return: label => INDPRO_yoy
                    #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
                    def __init__(self, year, label):
                    #@return: __init__ => None
                    #@inline 3: csv2df.util_row_splitter. split_row_by_periods 
                    def split_row_by_periods(row):
                    #@return: split_row_by_periods => ('', ['100,1', '', '', ''], ['...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 100.1
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2017-03-31 00:00:00
                    #@return: as_dict => {'year': 2017, 'label': 'INDPR...
                    #@return: make => {'year': 2017, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 102.3
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2017-01-31 00:00:00
                    #@return: as_dict => {'year': 2017, 'label': 'INDPR...
                    #@return: make => {'year': 2017, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 97.3
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2017-02-28 00:00:00
                    #@return: as_dict => {'year': 2017, 'label': 'INDPR...
                    #@return: make => {'year': 2017, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 100.8
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2017-03-31 00:00:00
                    #@return: as_dict => {'year': 2017, 'label': 'INDPR...
                    #@return: make => {'year': 2017, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 102.3
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2017-04-30 00:00:00
                    #@return: as_dict => {'year': 2017, 'label': 'INDPR...
                    #@return: make => {'year': 2017, 'label': 'INDPR...
                    #@inline 3: csv2df.emitter. DatapointMaker.make 
                    def make(self, freq: str, x: float, period=False):
                    #@inline 4: csv2df.emitter. DatapointMaker.set_value 
                    def set_value(self, x):
                    #@inline 5: csv2df.emitter. to_float 
                    def to_float(text: str, i=0):
                    #@return: to_float => 105.6
                    #@return: set_value => None
                    #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
                    def as_dict(self):
                    #@inline 5: csv2df.emitter. DatapointMaker.get_date 
                    def get_date(self):
                    #@return: get_date => 2017-05-31 00:00:00
                    #@return: as_dict => {'year': 2017, 'label': 'INDPR...
                    #@return: make => {'year': 2017, 'label': 'INDPR...
        #@return: _import => None
        #@inline 2: csv2df.emitter. _assert_defined 
        @staticmethod
        #@inline 3: csv2df.parser. Table.is_defined 
        def is_defined(self):
        #@inline 4: csv2df.parser. Table.label 
        @property
        #@inline 5: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_rog
        #@return: label => INDPRO_rog
        #@return: is_defined => True
        #@return: _assert_defined => None
        #@inline 2: csv2df.emitter. Emitter._import 
        def _import(self, table):
        #@inline 3: csv2df.reader. Row.get_year 
        def get_year(self):
        #@inline 4: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2015
        #@return: get_year => 2015
        #@inline 3: csv2df.parser. Table.label 
        @property
        #@inline 4: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_rog
        #@return: label => INDPRO_rog
        #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
        def __init__(self, year, label):
        #@return: __init__ => None
        #@inline 3: csv2df.util_row_splitter. split_row_by_periods 
        def split_row_by_periods(row):
        #@return: split_row_by_periods => ('', ['82,8', '102,6', '103,9'...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 82.8
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-03-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 102.6
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-06-30 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 103.9
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-09-30 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 112.3
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-12-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 73.9
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-01-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 99.8
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-02-28 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 112.5
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-03-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 95.6
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-04-30 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 97.6
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-05-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 103.2
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-06-30 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 100.5
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-07-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 101.4
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-08-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 103.1
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-09-30 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 105.0
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-10-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 101.9
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-11-30 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 109.1
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2015-12-31 00:00:00
        #@return: as_dict => {'year': 2015, 'label': 'INDPR...
        #@return: make => {'year': 2015, 'label': 'INDPR...
        #@inline 3: csv2df.reader. Row.get_year 
        def get_year(self):
        #@inline 4: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2016
        #@return: get_year => 2016
        #@inline 3: csv2df.parser. Table.label 
        @property
        #@inline 4: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_rog
        #@return: label => INDPRO_rog
        #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
        def __init__(self, year, label):
        #@return: __init__ => None
        #@inline 3: csv2df.util_row_splitter. split_row_by_periods 
        def split_row_by_periods(row):
        #@return: split_row_by_periods => ('', ['84,4', '103,1', '103,3'...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 84.4
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-03-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 103.1
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-06-30 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 103.3
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-09-30 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 113.1
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-12-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 74.7
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-01-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 104.4
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-02-29 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 108.8
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-03-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 96.3
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-04-30 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 98.1
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-05-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 103.8
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-06-30 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 99.9
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-07-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 101.5
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-08-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 101.7
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-09-30 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 106.6
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-10-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 103.6
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-11-30 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 105.8
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2016-12-31 00:00:00
        #@return: as_dict => {'year': 2016, 'label': 'INDPR...
        #@return: make => {'year': 2016, 'label': 'INDPR...
        #@inline 3: csv2df.reader. Row.get_year 
        def get_year(self):
        #@inline 4: csv2df.reader. get_year 
        def get_year(string: str, rx=YEAR_CATCHER):
        #@return: get_year => 2017
        #@return: get_year => 2017
        #@inline 3: csv2df.parser. Table.label 
        @property
        #@inline 4: csv2df.util_label. make_label 
        def make_label(vn, unit, sep=SEP):
        #@return: make_label => INDPRO_rog
        #@return: label => INDPRO_rog
        #@inline 3: csv2df.emitter. DatapointMaker.__init__ 
        def __init__(self, year, label):
        #@return: __init__ => None
        #@inline 3: csv2df.util_row_splitter. split_row_by_periods 
        def split_row_by_periods(row):
        #@return: split_row_by_periods => ('', ['83,1', '', '', ''], ['7...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 83.1
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2017-03-31 00:00:00
        #@return: as_dict => {'year': 2017, 'label': 'INDPR...
        #@return: make => {'year': 2017, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 76.2
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2017-01-31 00:00:00
        #@return: as_dict => {'year': 2017, 'label': 'INDPR...
        #@return: make => {'year': 2017, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 99.4
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2017-02-28 00:00:00
        #@return: as_dict => {'year': 2017, 'label': 'INDPR...
        #@return: make => {'year': 2017, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 112.7
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2017-03-31 00:00:00
        #@return: as_dict => {'year': 2017, 'label': 'INDPR...
        #@return: make => {'year': 2017, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 97.7
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2017-04-30 00:00:00
        #@return: as_dict => {'year': 2017, 'label': 'INDPR...
        #@return: make => {'year': 2017, 'label': 'INDPR...
        #@inline 3: csv2df.emitter. DatapointMaker.make 
        def make(self, freq: str, x: float, period=False):
        #@inline 4: csv2df.emitter. DatapointMaker.set_value 
        def set_value(self, x):
        #@inline 5: csv2df.emitter. to_float 
        def to_float(text: str, i=0):
        #@return: to_float => 101.2
        #@return: set_value => None
        #@inline 4: csv2df.emitter. DatapointMaker.as_dict 
        def as_dict(self):
        #@inline 5: csv2df.emitter. DatapointMaker.get_date 
        def get_date(self):
        #@return: get_date => 2017-05-31 00:00:00
        #@return: as_dict => {'year': 2017, 'label': 'INDPR...
        #@return: make => {'year': 2017, 'label': 'INDPR...
        #@return: _import => None
#@return: __init__ => None
#@inline 1: csv2df.emitter. Emitter.get_dataframe 
def get_dataframe(self, freq):
    df = pd.DataFrame(self._collect(freq)) # TRACE: freq, df.loc[:3]
    #@inline 2: csv2df.emitter. Emitter._collect 
    def _collect(self, freq):
        if freq in "aqm":
            return dict(a=self.a, q=self.q, m=self.m)[freq]
    #@return: _collect => [{'year': 2015, 'label': 'GDP_...
    if df.empty:
    self._assert_has_no_duplicate_rows(df)
    #@inline 2: csv2df.emitter. _assert_has_no_duplicate_rows 
    @staticmethod
        if df.empty:
            dups = df[df.duplicated(keep=False)]
        if not dups.empty:           #
    #@return: _assert_has_no_duplicate_rows => None
    df = df.pivot(columns='label', values='value', index='time_index') # TRACE: df
    df.insert(0, "year", df.index.year)
    if freq == "q":
    elif freq == "m":
    df.columns.name = None
    return df
#@return: get_dataframe =>             year  GDP_bln_rub ...
#@inline 1: csv2df.emitter. Emitter.get_dataframe 
def get_dataframe(self, freq):
#@inline 2: csv2df.emitter. Emitter._collect 
def _collect(self, freq):
#@return: _collect => [{'year': 2015, 'label': 'GDP_...
#@inline 2: csv2df.emitter. _assert_has_no_duplicate_rows 
@staticmethod
#@return: _assert_has_no_duplicate_rows => None
        df.insert(1, "qtr", df.index.quarter)
#@return: get_dataframe =>             year  qtr  GDP_bln...
#@inline 1: csv2df.emitter. Emitter.get_dataframe 
def get_dataframe(self, freq):
#@inline 2: csv2df.emitter. Emitter._collect 
def _collect(self, freq):
#@return: _collect => [{'year': 2015, 'label': 'INDP...
#@inline 2: csv2df.emitter. _assert_has_no_duplicate_rows 
@staticmethod
#@return: _assert_has_no_duplicate_rows => None
        df.insert(1, "month", df.index.month)
#@return: get_dataframe =>             year  month  INDPR...
