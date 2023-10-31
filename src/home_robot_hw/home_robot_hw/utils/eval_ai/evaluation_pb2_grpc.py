# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from home_robot_hw.utils.eval_ai import evaluation_pb2 as evaluation__pb2


class EnvironmentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.init_env = channel.unary_unary(
                '/evaluation.Environment/init_env',
                request_serializer=evaluation__pb2.Package.SerializeToString,
                response_deserializer=evaluation__pb2.Package.FromString,
                )
        self.number_of_episodes = channel.unary_unary(
                '/evaluation.Environment/number_of_episodes',
                request_serializer=evaluation__pb2.Package.SerializeToString,
                response_deserializer=evaluation__pb2.Package.FromString,
                )
        self.reset = channel.unary_unary(
                '/evaluation.Environment/reset',
                request_serializer=evaluation__pb2.Package.SerializeToString,
                response_deserializer=evaluation__pb2.Package.FromString,
                )
        self.get_current_episode = channel.unary_unary(
                '/evaluation.Environment/get_current_episode',
                request_serializer=evaluation__pb2.Package.SerializeToString,
                response_deserializer=evaluation__pb2.Package.FromString,
                )
        self.apply_action = channel.unary_unary(
                '/evaluation.Environment/apply_action',
                request_serializer=evaluation__pb2.Package.SerializeToString,
                response_deserializer=evaluation__pb2.Package.FromString,
                )
        self.evalai_update_submission = channel.unary_unary(
                '/evaluation.Environment/evalai_update_submission',
                request_serializer=evaluation__pb2.Package.SerializeToString,
                response_deserializer=evaluation__pb2.Package.FromString,
                )
        self.close = channel.unary_unary(
                '/evaluation.Environment/close',
                request_serializer=evaluation__pb2.Package.SerializeToString,
                response_deserializer=evaluation__pb2.Package.FromString,
                )


class EnvironmentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def init_env(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def number_of_episodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_current_episode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def apply_action(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def evalai_update_submission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnvironmentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'init_env': grpc.unary_unary_rpc_method_handler(
                    servicer.init_env,
                    request_deserializer=evaluation__pb2.Package.FromString,
                    response_serializer=evaluation__pb2.Package.SerializeToString,
            ),
            'number_of_episodes': grpc.unary_unary_rpc_method_handler(
                    servicer.number_of_episodes,
                    request_deserializer=evaluation__pb2.Package.FromString,
                    response_serializer=evaluation__pb2.Package.SerializeToString,
            ),
            'reset': grpc.unary_unary_rpc_method_handler(
                    servicer.reset,
                    request_deserializer=evaluation__pb2.Package.FromString,
                    response_serializer=evaluation__pb2.Package.SerializeToString,
            ),
            'get_current_episode': grpc.unary_unary_rpc_method_handler(
                    servicer.get_current_episode,
                    request_deserializer=evaluation__pb2.Package.FromString,
                    response_serializer=evaluation__pb2.Package.SerializeToString,
            ),
            'apply_action': grpc.unary_unary_rpc_method_handler(
                    servicer.apply_action,
                    request_deserializer=evaluation__pb2.Package.FromString,
                    response_serializer=evaluation__pb2.Package.SerializeToString,
            ),
            'evalai_update_submission': grpc.unary_unary_rpc_method_handler(
                    servicer.evalai_update_submission,
                    request_deserializer=evaluation__pb2.Package.FromString,
                    response_serializer=evaluation__pb2.Package.SerializeToString,
            ),
            'close': grpc.unary_unary_rpc_method_handler(
                    servicer.close,
                    request_deserializer=evaluation__pb2.Package.FromString,
                    response_serializer=evaluation__pb2.Package.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'evaluation.Environment', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Environment(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def init_env(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evaluation.Environment/init_env',
            evaluation__pb2.Package.SerializeToString,
            evaluation__pb2.Package.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def number_of_episodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evaluation.Environment/number_of_episodes',
            evaluation__pb2.Package.SerializeToString,
            evaluation__pb2.Package.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evaluation.Environment/reset',
            evaluation__pb2.Package.SerializeToString,
            evaluation__pb2.Package.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_current_episode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evaluation.Environment/get_current_episode',
            evaluation__pb2.Package.SerializeToString,
            evaluation__pb2.Package.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def apply_action(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evaluation.Environment/apply_action',
            evaluation__pb2.Package.SerializeToString,
            evaluation__pb2.Package.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def evalai_update_submission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evaluation.Environment/evalai_update_submission',
            evaluation__pb2.Package.SerializeToString,
            evaluation__pb2.Package.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evaluation.Environment/close',
            evaluation__pb2.Package.SerializeToString,
            evaluation__pb2.Package.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)