class resuable:
    
    def dropColumns(self,df,columns):
        df = df.drop(*columns)
        return df
    
    def dropDuplicates(self,df,columns):
        df = df.deduplicate(*columns)
        return df