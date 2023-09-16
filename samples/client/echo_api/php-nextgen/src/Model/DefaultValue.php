<?php
/**
 * DefaultValue
 *
 * PHP version 8.1
 *
 * @category Class
 * @package  OpenAPI\Client
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */

/**
 * Echo Server API
 *
 * Echo Server API
 *
 * The version of the OpenAPI document: 0.1.0
 * Contact: team@openapitools.org
 * @generated Generated by: https://openapi-generator.tech
 * OpenAPI Generator version: 7.0.1-SNAPSHOT
 */

/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

namespace OpenAPI\Client\Model;

use \ArrayAccess;
use \OpenAPI\Client\ObjectSerializer;

/**
 * DefaultValue Class Doc Comment
 *
 * @category Class
 * @description to test the default value of properties
 * @package  OpenAPI\Client
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 * @implements \ArrayAccess<string, mixed>
 */
class DefaultValue implements ModelInterface, ArrayAccess, \JsonSerializable
{
    public const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $openAPIModelName = 'DefaultValue';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $openAPITypes = [
        'array_string_enum_ref_default' => '\OpenAPI\Client\Model\StringEnumRef[]',
        'array_string_enum_default' => 'string[]',
        'array_string_default' => 'string[]',
        'array_integer_default' => 'int[]',
        'array_string' => 'string[]',
        'array_string_nullable' => 'string[]',
        'array_string_extension_nullable' => 'string[]',
        'string_nullable' => 'string'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      * @phpstan-var array<string, string|null>
      * @psalm-var array<string, string|null>
      */
    protected static $openAPIFormats = [
        'array_string_enum_ref_default' => null,
        'array_string_enum_default' => null,
        'array_string_default' => null,
        'array_integer_default' => null,
        'array_string' => null,
        'array_string_nullable' => null,
        'array_string_extension_nullable' => null,
        'string_nullable' => null
    ];

    /**
      * Array of nullable properties. Used for (de)serialization
      *
      * @var boolean[]
      */
    protected static array $openAPINullables = [
        'array_string_enum_ref_default' => false,
		'array_string_enum_default' => false,
		'array_string_default' => false,
		'array_integer_default' => false,
		'array_string' => false,
		'array_string_nullable' => true,
		'array_string_extension_nullable' => true,
		'string_nullable' => true
    ];

    /**
      * If a nullable field gets set to null, insert it here
      *
      * @var boolean[]
      */
    protected array $openAPINullablesSetToNull = [];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPITypes()
    {
        return self::$openAPITypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPIFormats()
    {
        return self::$openAPIFormats;
    }

    /**
     * Array of nullable properties
     *
     * @return array
     */
    protected static function openAPINullables(): array
    {
        return self::$openAPINullables;
    }

    /**
     * Array of nullable field names deliberately set to null
     *
     * @return boolean[]
     */
    private function getOpenAPINullablesSetToNull(): array
    {
        return $this->openAPINullablesSetToNull;
    }

    /**
     * Setter - Array of nullable field names deliberately set to null
     *
     * @param boolean[] $openAPINullablesSetToNull
     */
    private function setOpenAPINullablesSetToNull(array $openAPINullablesSetToNull): void
    {
        $this->openAPINullablesSetToNull = $openAPINullablesSetToNull;
    }

    /**
     * Checks if a property is nullable
     *
     * @param string $property
     * @return bool
     */
    public static function isNullable(string $property): bool
    {
        return self::openAPINullables()[$property] ?? false;
    }

    /**
     * Checks if a nullable property is set to null.
     *
     * @param string $property
     * @return bool
     */
    public function isNullableSetToNull(string $property): bool
    {
        return in_array($property, $this->getOpenAPINullablesSetToNull(), true);
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'array_string_enum_ref_default' => 'array_string_enum_ref_default',
        'array_string_enum_default' => 'array_string_enum_default',
        'array_string_default' => 'array_string_default',
        'array_integer_default' => 'array_integer_default',
        'array_string' => 'array_string',
        'array_string_nullable' => 'array_string_nullable',
        'array_string_extension_nullable' => 'array_string_extension_nullable',
        'string_nullable' => 'string_nullable'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'array_string_enum_ref_default' => 'setArrayStringEnumRefDefault',
        'array_string_enum_default' => 'setArrayStringEnumDefault',
        'array_string_default' => 'setArrayStringDefault',
        'array_integer_default' => 'setArrayIntegerDefault',
        'array_string' => 'setArrayString',
        'array_string_nullable' => 'setArrayStringNullable',
        'array_string_extension_nullable' => 'setArrayStringExtensionNullable',
        'string_nullable' => 'setStringNullable'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'array_string_enum_ref_default' => 'getArrayStringEnumRefDefault',
        'array_string_enum_default' => 'getArrayStringEnumDefault',
        'array_string_default' => 'getArrayStringDefault',
        'array_integer_default' => 'getArrayIntegerDefault',
        'array_string' => 'getArrayString',
        'array_string_nullable' => 'getArrayStringNullable',
        'array_string_extension_nullable' => 'getArrayStringExtensionNullable',
        'string_nullable' => 'getStringNullable'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$openAPIModelName;
    }

    public const ARRAY_STRING_ENUM_DEFAULT_SUCCESS = 'success';
    public const ARRAY_STRING_ENUM_DEFAULT_FAILURE = 'failure';
    public const ARRAY_STRING_ENUM_DEFAULT_UNCLASSIFIED = 'unclassified';

    /**
     * Gets allowable values of the enum
     *
     * @return string[]
     */
    public function getArrayStringEnumDefaultAllowableValues()
    {
        return [
            self::ARRAY_STRING_ENUM_DEFAULT_SUCCESS,
            self::ARRAY_STRING_ENUM_DEFAULT_FAILURE,
            self::ARRAY_STRING_ENUM_DEFAULT_UNCLASSIFIED,
        ];
    }

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->setIfExists('array_string_enum_ref_default', $data ?? [], null);
        $this->setIfExists('array_string_enum_default', $data ?? [], null);
        $this->setIfExists('array_string_default', $data ?? [], null);
        $this->setIfExists('array_integer_default', $data ?? [], null);
        $this->setIfExists('array_string', $data ?? [], null);
        $this->setIfExists('array_string_nullable', $data ?? [], null);
        $this->setIfExists('array_string_extension_nullable', $data ?? [], null);
        $this->setIfExists('string_nullable', $data ?? [], null);
    }

    /**
    * Sets $this->container[$variableName] to the given data or to the given default Value; if $variableName
    * is nullable and its value is set to null in the $fields array, then mark it as "set to null" in the
    * $this->openAPINullablesSetToNull array
    *
    * @param string $variableName
    * @param array  $fields
    * @param mixed  $defaultValue
    */
    private function setIfExists(string $variableName, array $fields, $defaultValue): void
    {
        if (self::isNullable($variableName) && array_key_exists($variableName, $fields) && is_null($fields[$variableName])) {
            $this->openAPINullablesSetToNull[] = $variableName;
        }

        $this->container[$variableName] = $fields[$variableName] ?? $defaultValue;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets array_string_enum_ref_default
     *
     * @return \OpenAPI\Client\Model\StringEnumRef[]|null
     */
    public function getArrayStringEnumRefDefault()
    {
        return $this->container['array_string_enum_ref_default'];
    }

    /**
     * Sets array_string_enum_ref_default
     *
     * @param \OpenAPI\Client\Model\StringEnumRef[]|null $array_string_enum_ref_default array_string_enum_ref_default
     *
     * @return self
     */
    public function setArrayStringEnumRefDefault($array_string_enum_ref_default)
    {
        if (is_null($array_string_enum_ref_default)) {
            throw new \InvalidArgumentException('non-nullable array_string_enum_ref_default cannot be null');
        }
        $this->container['array_string_enum_ref_default'] = $array_string_enum_ref_default;

        return $this;
    }

    /**
     * Gets array_string_enum_default
     *
     * @return string[]|null
     */
    public function getArrayStringEnumDefault()
    {
        return $this->container['array_string_enum_default'];
    }

    /**
     * Sets array_string_enum_default
     *
     * @param string[]|null $array_string_enum_default array_string_enum_default
     *
     * @return self
     */
    public function setArrayStringEnumDefault($array_string_enum_default)
    {
        if (is_null($array_string_enum_default)) {
            throw new \InvalidArgumentException('non-nullable array_string_enum_default cannot be null');
        }
        $allowedValues = $this->getArrayStringEnumDefaultAllowableValues();
        if (array_diff($array_string_enum_default, $allowedValues)) {
            throw new \InvalidArgumentException(
                sprintf(
                    "Invalid value for 'array_string_enum_default', must be one of '%s'",
                    implode("', '", $allowedValues)
                )
            );
        }
        $this->container['array_string_enum_default'] = $array_string_enum_default;

        return $this;
    }

    /**
     * Gets array_string_default
     *
     * @return string[]|null
     */
    public function getArrayStringDefault()
    {
        return $this->container['array_string_default'];
    }

    /**
     * Sets array_string_default
     *
     * @param string[]|null $array_string_default array_string_default
     *
     * @return self
     */
    public function setArrayStringDefault($array_string_default)
    {
        if (is_null($array_string_default)) {
            throw new \InvalidArgumentException('non-nullable array_string_default cannot be null');
        }
        $this->container['array_string_default'] = $array_string_default;

        return $this;
    }

    /**
     * Gets array_integer_default
     *
     * @return int[]|null
     */
    public function getArrayIntegerDefault()
    {
        return $this->container['array_integer_default'];
    }

    /**
     * Sets array_integer_default
     *
     * @param int[]|null $array_integer_default array_integer_default
     *
     * @return self
     */
    public function setArrayIntegerDefault($array_integer_default)
    {
        if (is_null($array_integer_default)) {
            throw new \InvalidArgumentException('non-nullable array_integer_default cannot be null');
        }
        $this->container['array_integer_default'] = $array_integer_default;

        return $this;
    }

    /**
     * Gets array_string
     *
     * @return string[]|null
     */
    public function getArrayString()
    {
        return $this->container['array_string'];
    }

    /**
     * Sets array_string
     *
     * @param string[]|null $array_string array_string
     *
     * @return self
     */
    public function setArrayString($array_string)
    {
        if (is_null($array_string)) {
            throw new \InvalidArgumentException('non-nullable array_string cannot be null');
        }
        $this->container['array_string'] = $array_string;

        return $this;
    }

    /**
     * Gets array_string_nullable
     *
     * @return string[]|null
     */
    public function getArrayStringNullable()
    {
        return $this->container['array_string_nullable'];
    }

    /**
     * Sets array_string_nullable
     *
     * @param string[]|null $array_string_nullable array_string_nullable
     *
     * @return self
     */
    public function setArrayStringNullable($array_string_nullable)
    {
        if (is_null($array_string_nullable)) {
            array_push($this->openAPINullablesSetToNull, 'array_string_nullable');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('array_string_nullable', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['array_string_nullable'] = $array_string_nullable;

        return $this;
    }

    /**
     * Gets array_string_extension_nullable
     *
     * @return string[]|null
     */
    public function getArrayStringExtensionNullable()
    {
        return $this->container['array_string_extension_nullable'];
    }

    /**
     * Sets array_string_extension_nullable
     *
     * @param string[]|null $array_string_extension_nullable array_string_extension_nullable
     *
     * @return self
     */
    public function setArrayStringExtensionNullable($array_string_extension_nullable)
    {
        if (is_null($array_string_extension_nullable)) {
            array_push($this->openAPINullablesSetToNull, 'array_string_extension_nullable');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('array_string_extension_nullable', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['array_string_extension_nullable'] = $array_string_extension_nullable;

        return $this;
    }

    /**
     * Gets string_nullable
     *
     * @return string|null
     */
    public function getStringNullable()
    {
        return $this->container['string_nullable'];
    }

    /**
     * Sets string_nullable
     *
     * @param string|null $string_nullable string_nullable
     *
     * @return self
     */
    public function setStringNullable($string_nullable)
    {
        if (is_null($string_nullable)) {
            array_push($this->openAPINullablesSetToNull, 'string_nullable');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('string_nullable', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['string_nullable'] = $string_nullable;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset): bool
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed|null
     */
    #[\ReturnTypeWillChange]
    public function offsetGet($offset)
    {
        return $this->container[$offset] ?? null;
    }

    /**
     * Sets value based on offset.
     *
     * @param int|null $offset Offset
     * @param mixed    $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value): void
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset): void
    {
        unset($this->container[$offset]);
    }

    /**
     * Serializes the object to a value that can be serialized natively by json_encode().
     * @link https://www.php.net/manual/en/jsonserializable.jsonserialize.php
     *
     * @return mixed Returns data which can be serialized by json_encode(), which is a value
     * of any type other than a resource.
     */
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
       return ObjectSerializer::sanitizeForSerialization($this);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        return json_encode(
            ObjectSerializer::sanitizeForSerialization($this),
            JSON_PRETTY_PRINT
        );
    }

    /**
     * Gets a header-safe presentation of the object
     *
     * @return string
     */
    public function toHeaderValue()
    {
        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}


