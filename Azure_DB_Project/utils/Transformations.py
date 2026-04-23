class reuse():

    def dropColumns(self, df, columns):
        return df.drop(*columns)
        