knn <- function (dataset, query, k) {

    classCol = ncol(dataset) # NUMERO DA ULTIMA COLUNA DE CLASSIFICADORES

    distanceVector = apply ( # VETOR DE DISTÂNCIA
        dataset,
        1, # PERCORRE AS LINHAS, 2 PERCORRE AS COLUNAS
        function (row) {
            sqrt (
				sum (
					(query - as.numeric(row[1:classCol-1])) ^2 # DISTÂNCIA EUCLIDIANA
				)
			)
        }
    )

    distanceVectorSorted = sort.list(distanceVector, dec=F)[1:k] # K VIZINHOS MAIS PRÓXIMOS
	classes = dataset [distanceVectorSorted, classCol] # CLASSIFICADORES POSSIVEIS
	
	result = list () # RESULTADO
	result$Classifiers = unique (classes) # CLASSIFICADORES DOS K VIZINHOS
	result$Value = rep (0, length (result$Classfiers)) # VETOR DE VOTOS
	
	for (i in 1:length(result$Classifiers)) {
		result$Value[i] = sum (result$Classifiers[i] == classes)
	}

	return (result)

}

