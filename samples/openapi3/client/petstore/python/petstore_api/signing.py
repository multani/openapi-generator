"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from base64 import b64encode
from Crypto.IO import PEM, PKCS8
from Crypto.Hash import SHA256, SHA512
from Crypto.Hash.SHA512 import SHA512Hash
from Crypto.Hash.SHA256 import SHA256Hash
from Crypto.PublicKey import RSA, ECC
from Crypto.Signature import PKCS1_v1_5, pss, DSS
from datetime import timedelta
from email.utils import formatdate
import os
import re
from time import time
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from typing_extensions import Protocol
from urllib.parse import urlencode, urlparse

# The constants below define a subset of HTTP headers that can be included in the
# HTTP signature scheme. Additional headers may be included in the signature.

# The '(request-target)' header is a calculated field that includes the HTTP verb,
# the URL path and the URL query.
HEADER_REQUEST_TARGET = '(request-target)'
# The time when the HTTP signature was generated.
HEADER_CREATED = '(created)'
# The time when the HTTP signature expires. The API server should reject HTTP requests
# that have expired.
HEADER_EXPIRES = '(expires)'
# The 'Host' header.
HEADER_HOST = 'Host'
# The 'Date' header.
HEADER_DATE = 'Date'
# When the 'Digest' header is included in the HTTP signature, the client automatically
# computes the digest of the HTTP request body, per RFC 3230.
HEADER_DIGEST = 'Digest'
# The 'Authorization' header is automatically generated by the client. It includes
# the list of signed headers and a base64-encoded signature.
HEADER_AUTHORIZATION = 'Authorization'

# The constants below define the cryptographic schemes for the HTTP signature scheme.
SCHEME_HS2019 = 'hs2019'
SCHEME_RSA_SHA256 = 'rsa-sha256'
SCHEME_RSA_SHA512 = 'rsa-sha512'

# The constants below define the signature algorithms that can be used for the HTTP
# signature scheme.
ALGORITHM_RSASSA_PSS = 'RSASSA-PSS'
ALGORITHM_RSASSA_PKCS1v15 = 'RSASSA-PKCS1-v1_5'

ALGORITHM_ECDSA_MODE_FIPS_186_3 = 'fips-186-3'
ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979 = 'deterministic-rfc6979'
ALGORITHM_ECDSA_KEY_SIGNING_ALGORITHMS = {
    ALGORITHM_ECDSA_MODE_FIPS_186_3,
    ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979
}

# The cryptographic hash algorithm for the message signature.
HASH_SHA256 = 'sha256'
HASH_SHA512 = 'sha512'


class ToJSONProtocol(Protocol):
    def to_json(self) -> str: ...


class HttpSigningConfiguration:
    """The configuration parameters for the HTTP signature security scheme.

    The HTTP signature security scheme is used to sign HTTP requests with a private key
    which is in possession of the API client.

    An ``Authorization`` header is calculated by creating a hash of select headers,
    and optionally the body of the HTTP request, then signing the hash value using
    a private key. The ``Authorization`` header is added to outbound HTTP requests.

    :param key_id: A string value specifying the identifier of the cryptographic key,
        when signing HTTP requests.
    :param signing_scheme: A string value specifying the signature scheme, when
        signing HTTP requests.
        Supported value are: ``hs2019``, ``rsa-sha256``, ``rsa-sha512``.
        Avoid using ``rsa-sha256``, ``rsa-sha512`` as they are deprecated. These values are
        available for server-side applications that only support the older
        HTTP signature algorithms.
    :param private_key_path: A string value specifying the path of the file containing
        a private key. The private key is used to sign HTTP requests.
    :param private_key_passphrase: A string value specifying the passphrase to decrypt
        the private key.
    :param signed_headers: A list of strings. Each value is the name of a HTTP header
        that must be included in the HTTP signature calculation.
        The two special signature headers ``(request-target)`` and ``(created)`` SHOULD be
        included in SignedHeaders.
        The ``(created)`` header expresses when the signature was created.
        The ``(request-target)`` header is a concatenation of the lowercased :method, an
        ASCII space, and the :path pseudo-headers.
        When signed_headers is not specified, the client defaults to a single value,
        ``(created)``, in the list of HTTP headers.
        When SignedHeaders contains the 'Digest' value, the client performs the
        following operations:
        1. Calculate a digest of request body, as specified in `RFC3230,
          section 4.3.2<https://datatracker.ietf.org/doc/html/rfc3230#section-4.3.2>`_.
        2. Set the ``Digest`` header in the request body.
        3. Include the ``Digest`` header and value in the HTTP signature.
    :param signing_algorithm: A string value specifying the signature algorithm, when
        signing HTTP requests.
        Supported values are:
        1. For RSA keys: RSASSA-PSS, RSASSA-PKCS1-v1_5.
        2. For ECDSA keys: fips-186-3, deterministic-rfc6979.
        If None, the signing algorithm is inferred from the private key.
        The default signing algorithm for RSA keys is RSASSA-PSS.
        The default signing algorithm for ECDSA keys is fips-186-3.
    :param hash_algorithm: The hash algorithm for the signature. Supported values are
        sha256 and sha512.
        If the signing_scheme is rsa-sha256, the hash algorithm must be set
        to None or sha256.
        If the signing_scheme is rsa-sha512, the hash algorithm must be set
        to None or sha512.
    :param signature_max_validity: The signature max validity, expressed as
        a datetime.timedelta value. It must be a positive value.
    """
    def __init__(self,
        key_id: str,
        signing_scheme: str,
        private_key_path: str,
        private_key_passphrase: Union[None, str]=None,
        signed_headers: Optional[List[str]]=None,
        signing_algorithm: Optional[str]=None,
        hash_algorithm: Optional[str]=None,
        signature_max_validity: Optional[timedelta]=None,
    ) -> None:
        self.key_id = key_id
        if signing_scheme not in {SCHEME_HS2019, SCHEME_RSA_SHA256, SCHEME_RSA_SHA512}:
            raise Exception("Unsupported security scheme: {0}".format(signing_scheme))
        self.signing_scheme = signing_scheme
        if not os.path.exists(private_key_path):
            raise Exception("Private key file does not exist")
        self.private_key_path = private_key_path
        self.private_key_passphrase = private_key_passphrase
        self.signing_algorithm = signing_algorithm
        self.hash_algorithm = hash_algorithm
        if signing_scheme == SCHEME_RSA_SHA256:
            if self.hash_algorithm is None:
                self.hash_algorithm = HASH_SHA256
            elif self.hash_algorithm != HASH_SHA256:
                raise Exception("Hash algorithm must be sha256 when security scheme is %s" %
                                SCHEME_RSA_SHA256)
        elif signing_scheme == SCHEME_RSA_SHA512:
            if self.hash_algorithm is None:
                self.hash_algorithm = HASH_SHA512
            elif self.hash_algorithm != HASH_SHA512:
                raise Exception("Hash algorithm must be sha512 when security scheme is %s" %
                                SCHEME_RSA_SHA512)
        elif signing_scheme == SCHEME_HS2019:
            if self.hash_algorithm is None:
                self.hash_algorithm = HASH_SHA256
            elif self.hash_algorithm not in {HASH_SHA256, HASH_SHA512}:
                raise Exception("Invalid hash algorithm")
        if signature_max_validity is not None and signature_max_validity.total_seconds() < 0:
            raise Exception("The signature max validity must be a positive value")
        self.signature_max_validity = signature_max_validity
        # If the user has not provided any signed_headers, the default must be set to '(created)',
        # as specified in the 'HTTP signature' standard.
        if signed_headers is None or len(signed_headers) == 0:
            signed_headers = [HEADER_CREATED]
        if self.signature_max_validity is None and HEADER_EXPIRES in signed_headers:
            raise Exception(
                "Signature max validity must be set when "
                "'(expires)' signature parameter is specified")
        if len(signed_headers) != len(set(signed_headers)):
            raise Exception("Cannot have duplicates in the signed_headers parameter")
        if HEADER_AUTHORIZATION in signed_headers:
            raise Exception("'Authorization' header cannot be included in signed headers")
        self.signed_headers = signed_headers
        self.private_key: Optional[Union[ECC.EccKey, RSA.RsaKey]] = None
        """The private key used to sign HTTP requests.
           Initialized when the PEM-encoded private key is loaded from a file.
        """
        self.host: Optional[str] = None
        """The host name, optionally followed by a colon and TCP port number.
        """
        self._load_private_key()

    def get_http_signature_headers(self, resource_path, method, headers, body, query_params):
        """Create a cryptographic message signature for the HTTP request and add the signed headers.

        :param resource_path : A string representation of the HTTP request resource path.
        :param method: A string representation of the HTTP request method, e.g. GET, POST.
        :param headers: A dict containing the HTTP request headers.
        :param body: The object representing the HTTP request body.
        :param query_params: A string representing the HTTP request query parameters.
        :return: A dict of HTTP headers that must be added to the outbound HTTP request.
        """
        if method is None:
            raise Exception("HTTP method must be set")
        if resource_path is None:
            raise Exception("Resource path must be set")

        signed_headers_list, request_headers_dict = self._get_signed_header_info(
            resource_path, method, headers, body, query_params)

        header_items = [
            "{0}: {1}".format(key.lower(), value) for key, value in signed_headers_list]
        string_to_sign = "\n".join(header_items)

        digest, digest_prefix = self._get_message_digest(string_to_sign.encode())
        b64_signed_msg = self._sign_digest(digest)

        request_headers_dict[HEADER_AUTHORIZATION] = self._get_authorization_header(
            signed_headers_list, b64_signed_msg)

        return request_headers_dict

    def get_public_key(self) -> Optional[Union[ECC.EccKey, RSA.RsaKey]]:
        """Returns the public key object associated with the private key.
        """
        pubkey: Optional[Union[ECC.EccKey, RSA.RsaKey]] = None
        if isinstance(self.private_key, RSA.RsaKey):
            pubkey = self.private_key.publickey()
        elif isinstance(self.private_key, ECC.EccKey):
            pubkey = self.private_key.public_key()
        return pubkey

    def _load_private_key(self) -> None:
        """Load the private key used to sign HTTP requests.
            The private key is used to sign HTTP requests as defined in
            https://datatracker.ietf.org/doc/draft-cavage-http-signatures/.
        """
        if self.private_key is not None:
            return
        with open(self.private_key_path, 'r') as f:
            pem_data = f.read()
            # Verify PEM Pre-Encapsulation Boundary
            r = re.compile(r"\s*-----BEGIN (.*)-----\s+")
            m = r.match(pem_data)
            if not m:
                raise ValueError("Not a valid PEM pre boundary")
            pem_header = m.group(1)
            if pem_header == 'RSA PRIVATE KEY':
                self.private_key = RSA.importKey(pem_data, self.private_key_passphrase)
            elif pem_header == 'EC PRIVATE KEY':
                self.private_key = ECC.import_key(pem_data, self.private_key_passphrase)
            elif pem_header in {'PRIVATE KEY', 'ENCRYPTED PRIVATE KEY'}:
                # Key is in PKCS8 format, which is capable of holding many different
                # types of private keys, not just EC keys.
                if self.private_key_passphrase is not None:
                    passphrase = self.private_key_passphrase.encode("utf-8")
                else:
                    passphrase = None
                (key_binary, pem_header, is_encrypted) = PEM.decode(pem_data, passphrase)
                (oid, privkey, params) = \
                    PKCS8.unwrap(key_binary, passphrase=self.private_key_passphrase)
                if oid == '1.2.840.10045.2.1':
                    self.private_key = ECC.import_key(pem_data, self.private_key_passphrase)
                else:
                    raise Exception("Unsupported key: {0}. OID: {1}".format(pem_header, oid))
            else:
                raise Exception("Unsupported key: {0}".format(pem_header))
            # Validate the specified signature algorithm is compatible with the private key.
            if self.signing_algorithm is not None:
                supported_algs = None
                if isinstance(self.private_key, RSA.RsaKey):
                    supported_algs = {ALGORITHM_RSASSA_PSS, ALGORITHM_RSASSA_PKCS1v15}
                elif isinstance(self.private_key, ECC.EccKey):
                    supported_algs = ALGORITHM_ECDSA_KEY_SIGNING_ALGORITHMS
                if supported_algs is not None and self.signing_algorithm not in supported_algs:
                    raise Exception(
                        "Signing algorithm {0} is not compatible with private key".format(
                            self.signing_algorithm))

    def _get_signed_header_info(
        self,
        resource_path: str,
        method: str,
        headers: Dict[str, str],
        body: Optional[ToJSONProtocol],
        query_params: Sequence[Tuple[Any, Any]],
    ) -> Tuple[
        List[Tuple[str, str]], # signature headers
        Dict[str, str], # request headers
    ]:
        """Build the HTTP headers (name, value) that need to be included in
        the HTTP signature scheme.

        :param resource_path : A string representation of the HTTP request resource path.
        :param method: A string representation of the HTTP request method, e.g. GET, POST.
        :param headers: A dict containing the HTTP request headers.
        :param body: The object (e.g. a dict) representing the HTTP request body.
        :param query_params: A string representing the HTTP request query parameters.
        :return: A tuple containing two dict objects:
            The first dict contains the HTTP headers that are used to calculate
            the HTTP signature.
            The second dict contains the HTTP headers that must be added to
            the outbound HTTP request.
        """

        if body is None:
            _body = ""
        else:
            _body = body.to_json()

        assert body is not None # help typing

        # Build the '(request-target)' HTTP signature parameter.
        assert self.host is not None
        target_host = urlparse(self.host).netloc
        target_path = urlparse(self.host).path
        request_target = method.lower() + " " + target_path + resource_path
        if query_params:
            request_target += "?" + urlencode(query_params)

        # Get UNIX time, e.g. seconds since epoch, not including leap seconds.
        now = time()
        # Format date per RFC 7231 section-7.1.1.2. An example is:
        # Date: Wed, 21 Oct 2015 07:28:00 GMT
        cdate = formatdate(timeval=now, localtime=False, usegmt=True)
        # The '(created)' value MUST be a Unix timestamp integer value.
        # Subsecond precision is not supported.
        created = int(now)
        if self.signature_max_validity is not None:
            expires = now + self.signature_max_validity.total_seconds()

        signed_headers_list = []
        request_headers_dict = {}

        value: Optional[str]
        for hdr_key in self.signed_headers:
            hdr_key = hdr_key.lower()
            if hdr_key == HEADER_REQUEST_TARGET:
                value = request_target
            elif hdr_key == HEADER_CREATED:
                value = '{0}'.format(created)
            elif hdr_key == HEADER_EXPIRES:
                value = '{0}'.format(expires)
            elif hdr_key == HEADER_DATE.lower():
                value = cdate
                request_headers_dict[HEADER_DATE] = '{0}'.format(cdate)
            elif hdr_key == HEADER_DIGEST.lower():
                request_body = _body.encode()
                body_digest, digest_prefix = self._get_message_digest(request_body)
                b64_body_digest = b64encode(body_digest.digest())
                value = digest_prefix + b64_body_digest.decode('ascii')
                request_headers_dict[HEADER_DIGEST] = '{0}{1}'.format(
                    digest_prefix, b64_body_digest.decode('ascii'))
            elif hdr_key == HEADER_HOST.lower():
                if isinstance(target_host, bytes):
                    value = target_host.decode('ascii')
                else:
                    value = target_host
                request_headers_dict[HEADER_HOST] = value
            else:
                value = next((v for k, v in headers.items() if k.lower() == hdr_key), None)
                if value is None:
                    raise Exception(
                        "Cannot sign HTTP request. "
                        "Request does not contain the '{0}' header".format(hdr_key))

            assert value is not None
            signed_headers_list.append((hdr_key, value))

        return signed_headers_list, request_headers_dict

    def _get_message_digest(self, data: bytes) -> Tuple[Union[SHA256Hash, SHA512Hash], str]:
        """Calculates and returns a cryptographic digest of a specified HTTP request.

        :param data: The string representation of the date to be hashed with a cryptographic hash.
        :return: A tuple of (digest, prefix).
            The digest is a hashing object that contains the cryptographic digest of
            the HTTP request.
            The prefix is a string that identifies the cryptographic hash. It is used
            to generate the 'Digest' header as specified in RFC 3230.
        """

        digest: Union[SHA256Hash, SHA512Hash]

        if self.hash_algorithm == HASH_SHA512:
            digest = SHA512.new()
            prefix = 'SHA-512='
        elif self.hash_algorithm == HASH_SHA256:
            digest = SHA256.new()
            prefix = 'SHA-256='
        else:
            raise Exception("Unsupported hash algorithm: {0}".format(self.hash_algorithm))
        digest.update(data)
        return digest, prefix

    def _sign_digest(self, digest: Union[SHA256Hash, SHA512Hash]) -> bytes:
        """Signs a message digest with a private key specified in the signing_info.

        :param digest: A hashing object that contains the cryptographic digest of the HTTP request.
        :return: A base-64 string representing the cryptographic signature of the input digest.
        """
        sig_alg = self.signing_algorithm
        if isinstance(self.private_key, RSA.RsaKey):
            if sig_alg is None or sig_alg == ALGORITHM_RSASSA_PSS:
                # RSASSA-PSS in Section 8.1 of RFC8017.
                signature = pss.new(self.private_key).sign(digest)
            elif sig_alg == ALGORITHM_RSASSA_PKCS1v15:
                # RSASSA-PKCS1-v1_5 in Section 8.2 of RFC8017.
                signature = PKCS1_v1_5.new(self.private_key).sign(digest)
            else:
                raise Exception("Unsupported signature algorithm: {0}".format(sig_alg))
        elif isinstance(self.private_key, ECC.EccKey):
            if sig_alg is None:
                sig_alg = ALGORITHM_ECDSA_MODE_FIPS_186_3
            if sig_alg in ALGORITHM_ECDSA_KEY_SIGNING_ALGORITHMS:
                # draft-ietf-httpbis-message-signatures-00 does not specify the ECDSA encoding.
                # Issue: https://github.com/w3c-ccg/http-signatures/issues/107
                signature = DSS.new(key=self.private_key, mode=sig_alg,
                                    encoding='der').sign(digest)
            else:
                raise Exception("Unsupported signature algorithm: {0}".format(sig_alg))
        else:
            raise Exception("Unsupported private key: {0}".format(type(self.private_key)))
        return b64encode(signature)

    def _get_authorization_header(
        self,
        signed_headers: List[Tuple[str, str]],
        signed_msg: bytes,
    ) -> str:
        """Calculates and returns the value of the 'Authorization' header when signing HTTP requests.

        :param signed_headers : A list of tuples. Each value is the name of a HTTP header that
            must be included in the HTTP signature calculation.
        :param signed_msg: A base-64 encoded string representation of the signature.
        :return: The string value of the 'Authorization' header, representing the signature
            of the HTTP request.
        """
        created_ts = None
        expires_ts = None
        for k, v in signed_headers:
            if k == HEADER_CREATED:
                created_ts = v
            elif k == HEADER_EXPIRES:
                expires_ts = v
        lower_keys = [k.lower() for k, v in signed_headers]
        headers_value = " ".join(lower_keys)

        auth_str = "Signature keyId=\"{0}\",algorithm=\"{1}\",".format(
                                                self.key_id, self.signing_scheme)
        if created_ts is not None:
            auth_str = auth_str + "created={0},".format(created_ts)
        if expires_ts is not None:
            auth_str = auth_str + "expires={0},".format(expires_ts)
        auth_str = auth_str + "headers=\"{0}\",signature=\"{1}\"".format(
                                                headers_value, signed_msg.decode('ascii'))

        return auth_str
