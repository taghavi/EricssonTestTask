#Method1
# FROM microsoft/dotnet AS build-env
# WORKDIR /App
# COPY *.csproj ./
# RUN dotnet restore
# COPY . ./
# RUN dotnet publish -c Release -o out
# WORKDIR /App
# #COPY bin/Release/netcoreapp2.1/publish/ App/
# COPY --from=build-env /App/out .
# ENTRYPOINT ["dotnet", "Client.dll"]

#Method2 faster
FROM microsoft/dotnet
ENV MY_SERVER="server"
COPY bin/release/netcoreapp2.1/publish/ App/
WORKDIR /App
ENTRYPOINT ["dotnet", "Client.dll"]