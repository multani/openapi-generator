=begin
#OpenAPI Extension generating aliases to maps and arrays as models

#This specification shows how to generate aliases to maps and arrays as models.

The version of the OpenAPI document: 1.0.0

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 7.0.1-SNAPSHOT

=end

# Common files
require 'petstore/api_client'
require 'petstore/api_error'
require 'petstore/version'
require 'petstore/configuration'

# Models
require 'petstore/models/map_alias'
require 'petstore/models/array_alias'

# APIs
require 'petstore/api/usage_api'

module Petstore
  class << self
    # Customize default settings for the SDK using block.
    #   Petstore.configure do |config|
    #     config.username = "xxx"
    #     config.password = "xxx"
    #   end
    # If no block given, return the default Configuration object.
    def configure
      if block_given?
        yield(Configuration.default)
      else
        Configuration.default
      end
    end
  end
end
